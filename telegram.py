import asyncio
import os
from telethon import TelegramClient, events
from telethon.tl.types import DocumentAttributeFilename
import log
import database
import pdfff
from custom_event import CustomEvent
from dto.mapped_message import MappedMessageDTO
from configs import base
from formatter import replace_emodji, remove_text


class TelegramChannelSync:
    def __init__(self, account_name, account_session, api_id, api_hash, channels_links):
        self.client = None
        self.account_name = account_name
        self.account_session = account_session
        self.api_id = api_id
        self.api_hash = api_hash
        self.logger = log.get_logger_by_account(account_name)
        self.channel_links = channels_links
        self.source_channels = list(channels_links.keys())
        self.new_message_queues = {}

    async def run(self):
        try:
            self.client = TelegramClient(self.account_session, self.api_id, self.api_hash)
            await self.client.start()
            self.logger.info("Клиент Telegram успешно запущен")
            tasks = self._set_queues()
            await self._missed_messages()
            self._setup_handlers()
            try:
                await self.client.run_until_disconnected()
            finally:
                for task in tasks:
                    task.cancel()
        except Exception as e:
            self.logger.exception(f"Произошла ошибка: {e}")

    def _setup_handlers(self):
        self.client.on(events.NewMessage(chats=self.source_channels))(self._new_message_handler)
        self.client.on(events.MessageEdited(chats=self.source_channels))(self._edit_message_handler)
        self.client.on(events.MessageDeleted(chats=self.source_channels))(self._delete_message_handler)

    async def _process_new_message(self, queue):
        while True:
            event = await queue.get()

            try:
                file_path = await self._download_pdf(event)

                link = self.channel_links[event.chat_id]
                event.message.message, event.message.entities = replace_emodji(
                    event.message.message,
                    link['emojis_for_replace'],
                    event.message.entities
                )
                event.message.message, event.message.entities = remove_text(
                    event.message.message,
                    link['text_for_remove'],
                    event.message.entities
                )
                for target in link['target']:
                    if file_path is not None:
                        result_path = await self._add_watermark_to_pdf(
                            link['pdf_watermark'][target],
                            target,
                            file_path
                        )

                        sent_message = await self.client.send_file(
                            target,
                            result_path,
                            caption=event.message.message,
                            formatting_entities=event.message.entities
                        )
                        self._remove_pdf(result_path)
                    else:
                        if event.message.message != '' or (event.message.message == '' and event.message.media):
                            sent_message = await self.client.send_message(target, event.message)
                        else:
                            break

                    database.insert_mapped_message(self.account_name, event.chat_id, event.message.id, target, sent_message.id)
                    self.logger.info('Сообщение [{}] отправлено в канал [{}].'.format(event.message.id, target))

                if file_path:
                    self._remove_pdf(file_path)

                database.insert_last_message(self.account_name, event.chat_id, event.message.id)
            except Exception as e:
                self.logger.exception(f"Ошибка при пересылке сообщения: {e}")
            finally:
                queue.task_done()

    async def _new_message_handler(self, event):
        last_message_data = database.get_last_messages_by_channel(event.chat_id)
        if last_message_data is not None:
            account_name_, channel_id, message_id = last_message_data
            if event.message.id <= message_id:
                return

        queue = self.new_message_queues[event.chat_id]
        await queue.put(event)

    async def _edit_message_handler(self, event):
        self.logger.info('В канале [{}] было изменено сообщение [{}.'.format(event.chat_id, event.message.id))

        link = self.channel_links[event.chat_id]
        for target in link['target']:
            event.message.message, event.message.entities = replace_emodji(
                event.message.message,
                link['emojis_for_replace'],
                event.message.entities
            )
            event.message.message, event.message.entities = remove_text(
                event.message.message,
                link['text_for_remove'],
                event.message.entities
            )

            mapped_massage = self._get_mapped_message_dto(self.account_name, event.chat_id, event.message.id, target)

            await self.client.edit_message(
                target,
                mapped_massage.target_message_id,
                event.message.message,
                file=event.message.media,
                formatting_entities=event.message.entities
            )

            self.logger.info('Сообщение [{}] было отредактировано к канале [{}].'.format(event.message.id, target))

    async def _delete_message_handler(self, event):
        for deleted_id in event.deleted_ids:
            self.logger.info('В канале [{}] было удаленно сообщение [{}].'.format(event.chat_id, deleted_id))

            link = self.channel_links[event.chat_id]
            for target in link['target']:
                mapped_massage = self._get_mapped_message_dto(self.account_name, event.chat_id, deleted_id, target)
                await self.client.delete_messages(target, [mapped_massage.target_message_id])
                database.delete_mapped_message(
                    self.account_name,
                    event.chat_id,
                    deleted_id,
                    target,
                    mapped_massage.target_message_id
                )

                self.logger.info('Сообщение [{}] удалено в канале [{}]'.format(deleted_id, target))

    async def _missed_messages(self):
        last_messages = database.get_last_messages_by_acc(self.account_name)
        for last_message in last_messages:
            account_name, channel_id, message_id = last_message

            if channel_id not in self.source_channels:
                continue

            link = self.channel_links[channel_id]
            if not link['send_missed_messages']['enable']:
                continue

            count = link['send_missed_messages']['count']
            last_message_in_channel = await self.client.get_messages(channel_id, limit=1)

            if message_id == last_message_in_channel[0].id:
                continue

            if last_message_in_channel[0].id - message_id <= count:
                iter_messages = self.client.iter_messages(channel_id, offset_id=message_id, reverse=True)
            else:
                offset_id = last_message_in_channel[0].id - count
                iter_messages = self.client.iter_messages(channel_id, offset_id=offset_id, reverse=True)

            async for message in iter_messages:
                custom_event = CustomEvent(channel_id, message)
                await self._new_message_handler(custom_event)
                await asyncio.sleep(3)

    def _set_queues(self):
        tasks = []
        for channel_id in self.source_channels:
            self.new_message_queues[channel_id] = asyncio.Queue()
            tasks.append(
                self.client.loop.create_task(
                    self._process_new_message(
                        self.new_message_queues[channel_id]
                    )
                )
            )

        return tasks

    async def _download_pdf(self, event):
        try:
            has_pdf = event.message.document and 'application/pdf' in event.message.document.mime_type
            if not has_pdf:
                return None

            file_name = None
            for attribute in event.message.media.document.attributes:
                if isinstance(attribute, DocumentAttributeFilename):
                    file_name = attribute.file_name
                    self.logger.info(f"Обнаружен файл: {file_name}")
                    break

            if file_name is None:
                self.logger.exception("Название файла не обнаружено")
                return None

            file_path = str(await self.client.download_media(
                event.message,
                file=f'{base.DOWNLOAD_PATH}/{event.chat_id}/{event.message.id}/{file_name}'
            ))

            self.logger.info(f"Скачан PDF-файл: {file_path}")
            return file_path
        except Exception as e:
            self.logger.exception(f"Ошибка при скачивании PDF-файла: {e}")

    async def _add_watermark_to_pdf(self, watermark_config, target, file_path):
        try:
            target_dir = os.path.dirname(file_path) + f"/{target}"
            os.mkdir(target_dir)
            result = target_dir + "/" + os.path.basename(file_path)

            await pdfff.add_watermark(
                file_path,
                watermark_config['path'],
                result,
                watermark_config['scale'],
                watermark_config['angle'],
                watermark_config['opacity'],
            )
            self.logger.info(f"На PDF-файл {file_path}, добавлена watermark-а: {watermark_config['path']}")
            return result
        except Exception as e:
            self.logger.exception(f"Ошибка при добавлении watermark-и: {e}")

    def _remove_pdf(self, file_path):
        try:
            os.remove(file_path)

            first_parent_folder = os.path.dirname(file_path)
            if not os.listdir(first_parent_folder):
                os.rmdir(first_parent_folder)

            self.logger.info(f"PDF-файл удален: {file_path}")
        except Exception as e:
            self.logger.exception(f"Ошибка при удалении PDF-файла: {e}")

    @staticmethod
    def _get_mapped_message_dto(account_name, source_channel_id, source_message_id, target_channel_id):
        mapped_massage_response = database.get_mapped_message_by(
            account_name,
            source_channel_id,
            source_message_id,
            target_channel_id
        )

        return MappedMessageDTO(mapped_massage_response)

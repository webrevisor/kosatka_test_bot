import asyncio

from telethon import TelegramClient, events
from telethon.tl.types import DocumentAttributeFilename
from logger import logger
import config
import pdfff
import os
from database import conn, cursor
from custom_event import CustomEvent


class TelegramChannelSync:
    def __init__(self, api_id, api_hash, channel_links):
        self.client = TelegramClient('session_name', api_id, api_hash)
        self.channel_links = channel_links
        self.mapped_channels = {}  # Словарь для отслеживания ID сообщений
        self.message_ids = {}  # Словарь для отслеживания ID сообщений
        self.new_message_queues = {}

    async def run(self):
        try:
            await self.client.start()

            logger.info("Клиент Telegram успешно запущен")
            self._set_mapped_channels()
            tasks = self._set_queues()
            await self._missed_messages()
            self._setup_handlers()
            try:
                await self.client.run_until_disconnected()
            finally:
                for task in tasks:
                    task.cancel()
        except Exception as e:
            logger.exception(f"Произошла ошибка: {e}")

    def _set_queues(self):
        tasks = []
        for channel_id in list(self.mapped_channels.keys()):
            self.new_message_queues[channel_id] = asyncio.Queue()
            tasks.append(
                self.client.loop.create_task(
                    self.process_new_message_queue(
                        self.new_message_queues[channel_id]
                    )
                )
            )

        return tasks

    def _set_mapped_channels(self):
        for link in self.channel_links:
            for source_id in link['source']:
                if source_id in self.mapped_channels:
                    # Объединяем списки, если исходный канал уже есть в результате
                    self.mapped_channels[source_id]['target'] = list(set(self.mapped_channels[source_id] + link['target']))
                else:
                    # Создаем новую запись, если исходного канала еще нет в результате
                    self.mapped_channels[source_id] = {'target': link['target']}

                self.mapped_channels[source_id]['send_missed_messages'] = link['send_missed_messages']

    async def _missed_messages(self):
        # Выполнение запроса на выборку данных из таблицы
        cursor.execute('SELECT * FROM last_messages')

        # Извлечение всех записей
        records = cursor.fetchall()
        for record in records:
            channel_id, message_id = record

            if channel_id not in self.mapped_channels:
                continue

            if not self.mapped_channels[channel_id]['send_missed_messages']['enable']:
                continue

            count = self.mapped_channels[channel_id]['send_missed_messages']['count']
            last_messages = await self.client.get_messages(channel_id, limit=1)

            if message_id == last_messages[0].id:
                continue

            if last_messages[0].id - message_id <= count:
                iter_messages = self.client.iter_messages(channel_id, offset_id=message_id, reverse=True)
            else:
                offset_id = last_messages[0].id - count
                iter_messages = self.client.iter_messages(channel_id, offset_id=offset_id, reverse=True)

            async for message in iter_messages:
                custom_event = CustomEvent(channel_id, message)
                await self._new_message_handler(custom_event)
                await asyncio.sleep(3)

    def _setup_handlers(self):
        self.client.on(events.NewMessage(chats=self._get_source_channels()))(self._new_message_handler)
        self.client.on(events.MessageEdited(chats=self._get_source_channels()))(self._edit_message_handler)
        self.client.on(events.MessageDeleted(chats=self._get_source_channels()))(self._delete_message_handler)

    def _get_source_channels(self):
        return list(set([channel for link in self.channel_links for channel in link['source']]))

    async def _download_pdf(self, event):
        try:
            has_pdf = event.message.document and 'application/pdf' in event.message.document.mime_type
            if not has_pdf:
                return None

            file_name = None
            for attribute in event.message.media.document.attributes:
                if isinstance(attribute, DocumentAttributeFilename):
                    file_name = attribute.file_name
                    logger.info(f"Обнаружен файл: {file_name}")
                    break

            if file_name is None:
                logger.exception("Название файла не обнаружено")
                return None

            file_path = str(await self.client.download_media(
                event.message,
                file=f'{config.PDF_DOWNLOAD_DIRECTORY}/{event.chat_id}/{event.message.id}/{file_name}'
            ))

            logger.info(f"Скачан PDF-файл: {file_path}")
            return file_path
        except Exception as e:
            logger.exception(f"Ошибка при скачивании PDF-файла: {e}")

    @staticmethod
    def _remove_pdf(file_path):
        try:
            # Удаление файла
            os.remove(file_path)

            # Проверка и удаление первой вложенной папки, если она пуста
            first_parent_folder = os.path.dirname(file_path)
            if not os.listdir(first_parent_folder):  # Проверка, пуста ли папка
                os.rmdir(first_parent_folder)

            logger.info(f"PDF-файл удален: {file_path}")
        except Exception as e:
            logger.exception(f"Ошибка при удалении PDF-файла: {e}")

    @staticmethod
    async def _add_watermark_to_pdf(watermark_config, target, file_path):
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
            logger.info(f"На PDF-файл {file_path}, добавлена watermark-а: {watermark_config['path']}")
            return result
        except Exception as e:
            logger.exception(f"Ошибка при добавлении watermark-и: {e}")

    @staticmethod
    def _emojis_replace(text, emoji_replacement):
        try:
            for search_emoji, replacement in emoji_replacement.items():
                text = text.replace(search_emoji, replacement)
            return text.strip()
        except Exception as e:
            logger.exception(f"Ошибка при изменении Emoji: {e}")

    @staticmethod
    def _remove_text(text, remove_text, entities):

        formatted_remove_text = remove_text + "\n"
        formatted_remove_text_offset_start = text.find(formatted_remove_text)
        if formatted_remove_text_offset_start == -1:
            formatted_remove_text = remove_text + " "
            formatted_remove_text_offset_start = text.find(formatted_remove_text)
            if formatted_remove_text_offset_start == -1:
                formatted_remove_text = remove_text
                formatted_remove_text_offset_start = text.find(formatted_remove_text)

        if formatted_remove_text_offset_start == -1:
            return text, entities

        formatted_text_with_removed_text = text.replace(formatted_remove_text, '')
        call_plus = len(formatted_text_with_removed_text) - len(formatted_text_with_removed_text.strip())
        formatted_remove_text_length = len(formatted_remove_text) + call_plus
        formatted_remove_text_offset_end = formatted_remove_text_offset_start + formatted_remove_text_length

        formatted_entities = []
        minus = 0
        if entities is None:
            return formatted_text_with_removed_text, None

        for entity in entities:
            entity.offset -= minus
            entity_offset_end = entity.offset + entity.length

            if entity.offset == formatted_remove_text_offset_start and entity.length == formatted_remove_text_length:
                continue

            if formatted_remove_text_offset_start < entity.offset or formatted_remove_text_offset_start > entity_offset_end:
                formatted_entities.append(entity)
                continue

            if formatted_remove_text_offset_end < entity_offset_end:
                minus = formatted_remove_text_length + 1
                entity.length -= minus
                formatted_entities.append(entity)
                continue

            minus = entity_offset_end - formatted_remove_text_offset_start + 1
            entity.length -= minus
            formatted_entities.append(entity)

        return formatted_text_with_removed_text, formatted_entities

    async def process_new_message_queue(self, new_message_queue):
        while True:
            # Получаем событие из очереди
            event = await new_message_queue.get()

            try:
                file_path = await self._download_pdf(event)

                for link in self.channel_links:
                    if event.chat_id in link['source']:
                        formatted_text = self._emojis_replace(event.message.message, link['emojis_replacement'])
                        formatted_text, formatted_entities = self._remove_text(formatted_text, link['text_remove'],
                                                                               event.message.entities)

                        if formatted_text == '':
                            event.message.message = None
                        else:
                            event.message.message = formatted_text

                        event.message.entities = formatted_entities

                        for target in link['target']:
                            if file_path is not None:
                                result_path = await self._add_watermark_to_pdf(link['pdf_watermark'][target], target,
                                                                               file_path)
                                sent_message = await self.client.send_file(
                                    target,
                                    result_path,
                                    caption=event.message.message,
                                    formatting_entities=event.message.entities
                                )
                                self._remove_pdf(result_path)
                            else:
                                if formatted_text != '' or (formatted_text == '' and event.message.media):
                                    sent_message = await self.client.send_message(target, event.message)
                                else:
                                    break
                            self._update_message_ids(event.chat_id, event.message.id, target, sent_message.id)
                            logger.info(
                                f"Новое сообщение [{event.message.id}] из [{event.chat_id}] переслано в [{target}]")

                if file_path:
                    self._remove_pdf(file_path)

                # Выполнение запроса на выборку данных из таблицы
                cursor.execute(f'SELECT * FROM last_messages WHERE channel_id = {event.chat_id}')
                last_message_data = cursor.fetchone()
                if last_message_data is None:
                    cursor.execute('''
                            INSERT OR REPLACE INTO last_messages (channel_id, message_id)
                            VALUES (?, ?)
                        ''', (event.chat_id, event.message.id))
                else:
                    channel_id, message_id = last_message_data
                    if message_id < event.message.id:
                        cursor.execute('''
                                INSERT OR REPLACE INTO last_messages (channel_id, message_id)
                                VALUES (?, ?)
                            ''', (event.chat_id, event.message.id))
                conn.commit()
            except Exception as e:
                logger.exception(f"Ошибка при пересылке сообщения: {e}")
            finally:
                # Помечаем задачу как выполненную
                new_message_queue.task_done()

    async def _new_message_handler(self, event):
        new_message_queue = self.new_message_queues[event.chat_id]
        await new_message_queue.put(event)

    async def _edit_message_handler(self, event):
        try:
            for link in self.channel_links:
                if event.chat_id in link['source']:
                    formatted_text = self._emojis_replace(event.message.message, link['emojis_replacement'])
                    event.message.message = formatted_text
                    for target in link['target']:
                        if (event.chat_id, event.message.id, target) in self.message_ids:
                            target_msg_id = self.message_ids[(event.chat_id, event.message.id, target)]
                            await self.client.edit_message(target, target_msg_id, event.message.message,
                                                           file=event.message.media,
                                                           formatting_entities=event.message.entities)
                            logger.info(
                                f"Сообщение [{event.message.id}] отредактировано в [{event.chat_id}] и обновлено в [{target}]")
        except Exception as e:
            logger.exception(f"Ошибка при редактировании сообщения: {e}")

    async def _delete_message_handler(self, event):
        try:
            for deleted_id in event.deleted_ids:
                for link in self.channel_links:
                    if event.chat_id in link['source']:
                        for target in link['target']:
                            if (event.chat_id, deleted_id, target) in self.message_ids:
                                target_msg_id = self.message_ids[(event.chat_id, deleted_id, target)]
                                await self.client.delete_messages(target, [target_msg_id])
                                logger.info(f"Сообщение [{deleted_id}] из [{event.chat_id}] удалено в [{target}]")
        except Exception as e:
            logger.exception(f"Ошибка при удалении сообщения: {e}")

    def _update_message_ids(self, source_chat_id, source_msg_id, target_chat_id, target_msg_id):
        self.message_ids[(source_chat_id, source_msg_id, target_chat_id)] = target_msg_id

import asyncio
from configs import second
from telegram import TelegramChannelSync
import database

sync_bot = TelegramChannelSync(
    second.ACCOUNT_NAME,
    second.ACCOUNT_SESSION,
    second.API_ID,
    second.API_HASH,
    second.CHANNELS_LINKS
)


async def main():
    # Запуск обеих функций параллельно
    await asyncio.gather(
        clear_mapped_messages(),
        sync_bot.run()
    )


async def clear_mapped_messages():
    while True:
        for channel in sync_bot.source_channels:
            messages = database.get_mapped_messages_by_acc_channel(second.ACCOUNT_NAME, channel)
            ids = [t[0] for t in messages]
            if len(ids) > 100:
                ids = ids[:-100] if len(ids) > 100 else ids
                database.remove_mapped_messages(ids)
        await asyncio.sleep(60 * 5)

asyncio.run(main())

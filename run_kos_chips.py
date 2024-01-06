import asyncio
from configs import kos_chips
from telegram import TelegramChannelSync
import database

sync_bot = TelegramChannelSync(
    kos_chips.ACCOUNT_NAME,
    kos_chips.ACCOUNT_SESSION,
    kos_chips.API_ID,
    kos_chips.API_HASH,
    kos_chips.CHANNELS_LINKS
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
            messages = database.get_mapped_messages_by_acc_channel(kos_chips.ACCOUNT_NAME, channel)
            ids = [t[0] for t in messages]
            if len(ids) > 100:
                ids = ids[:-100] if len(ids) > 100 else ids
                database.remove_mapped_messages(ids)
        await asyncio.sleep(60 * 5)

asyncio.run(main())

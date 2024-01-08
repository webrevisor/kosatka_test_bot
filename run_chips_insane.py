import asyncio
import tasker
from configs import chips_insane
from telegram import TelegramChannelSync

sync_bot = TelegramChannelSync(
    chips_insane.ACCOUNT_NAME,
    chips_insane.ACCOUNT_SESSION,
    chips_insane.API_ID,
    chips_insane.API_HASH,
    chips_insane.CHANNELS_LINKS
)


async def main():
    await asyncio.gather(
        tasker.clear_mapped_messages(
            sync_bot.channel_links,
            chips_insane.ACCOUNT_NAME,
            chips_insane.base.SYNC_MESSAGES_COUNT
        ),
        sync_bot.run()
    )

asyncio.run(main())

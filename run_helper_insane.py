import asyncio
from configs import helper_insane
from telegram import TelegramChannelSync
import tasker

sync_bot = TelegramChannelSync(
    helper_insane.ACCOUNT_NAME,
    helper_insane.ACCOUNT_SESSION,
    helper_insane.API_ID,
    helper_insane.API_HASH,
    helper_insane.CHANNELS_LINKS
)


async def main():
    await asyncio.gather(
        tasker.clear_mapped_messages(
            sync_bot.channel_links,
            helper_insane.ACCOUNT_NAME,
            helper_insane.base.SYNC_MESSAGES_COUNT
        ),
        sync_bot.run()
    )

asyncio.run(main())

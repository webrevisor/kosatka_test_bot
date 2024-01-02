import asyncio
import config
from telegram import TelegramChannelSync

sync_bot = TelegramChannelSync(
    config.API_ID,
    config.API_HASH,
    config.CHANNELS_LINKS
)

asyncio.run(sync_bot.run())

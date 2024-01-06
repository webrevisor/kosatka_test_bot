import asyncio
from configs import kos_chips
from telegram import TelegramChannelSync

sync_bot = TelegramChannelSync(
    kos_chips.ACCOUNT_NAME,
    kos_chips.ACCOUNT_SESSION,
    kos_chips.API_ID,
    kos_chips.API_HASH,
    kos_chips.CHANNELS_LINKS
)

asyncio.run(sync_bot.run())

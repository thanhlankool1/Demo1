from aiogram import Bot, Dispatcher
from app.configs import settings


# if settings.APP_USE_PROXY:
#     bot = Bot(token=settings.APP_TELEGRAM_BOT_TOKEN, proxy=settings.APP_PROXY_SERVER)
# else:
bot = Bot(token=settings.APP_TELEGRAM_BOT_TOKEN)

dp = Dispatcher(bot)


async def telegram_send_message(msg: str, channel: str = settings.APP_TELEGRAM_NOTIFICATION_CHANNEL):
    await bot.send_message(channel, msg)
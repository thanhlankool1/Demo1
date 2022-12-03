#-*- coding: utf-8 -*-
from app.utils.telegram_bot import telegram_send_message


async def event_01_disconnect_database():
    pass


async def event_99_notify_app_stopped():
    await telegram_send_message('LanLT23 Demo Stop App')


events = [v for k, v in locals().items() if k.startswith('event_')]

#-*- coding: utf-8 -*-
from app.utils.telegram_bot import telegram_send_message

async def event_01_notification_telegram():
    print("vào đây không")
    await telegram_send_message('LanLT23 Demo Start App')


events = [v for k, v in locals().items() if k.startswith('event_')]
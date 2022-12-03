# -*- coding: utf-8 -*-
from fastapi import FastAPI
from .api import app as api_app
from .ws import initialize_socketio_event_handlers, socketio_app
from app.event_app import start_events, stop_events


app = FastAPI(
    docs_url=None,
    on_startup=start_events,
    on_shutdown=stop_events
    )


# mount websocket
app.mount("/ws", socketio_app)
initialize_socketio_event_handlers()


# mount api app
app.mount("/", api_app)
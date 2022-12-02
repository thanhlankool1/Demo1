from celery import Celery
import asyncio
from app.configs import settings
import time
from app.utils.logger import logger

config = {
    'CELERY_RESULT_BACKEND': f'redis://{settings.REDIS_SERVER}:{settings.REDIS_PORT}/1',
}
DEMO = Celery(
    'celery_demo_app',
    broker="redis://localhost:6379/0",
    result_backend="redis://localhost:6379/0",
    result_expires=3600)

@DEMO.task(
    bind=True,
    trail=True,
)
def first_task(self, data, **kwargs):
    print(data)
    return {
        "username" : data.get("name", "none name"),
        "email" : data.get("name", "none name") + "@fpt.com.vn",
        "delay" : data.get("delay", 5)
    }

@DEMO.task(
    bind=True,
    trail=True,
)
def save_to_mongo(self, data):
    time.sleep(data.get("delay"))
    logger.critical(data)
    return True
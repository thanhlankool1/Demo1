# -*- coding: utf-8 -*
import uvloop
import uvicorn
from app.configs import settings

uvloop.install()

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        loop='uvloop',
        reload=True,
        host=settings.GUNICORN_HOST,
        port=int(settings.GUNICORN_PORT),
        timeout_keep_alive=0,
    )
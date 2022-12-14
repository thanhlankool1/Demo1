# -*- coding: utf-8 -*-
from typing import Optional, List, Union, Tuple
from pydantic import BaseSettings, AnyHttpUrl
import os

class AppEnvConfig(BaseSettings):
    APP_BASE_DIR: Optional[str] = os.getcwd()
    APP_PROJECT_NAME: str = "FastApi-App"
    APP_DEBUG: bool = True
    APP_USE_PROXY: bool = False
    APP_PROXY_SERVER: str = ""
    APP_NO_PROXY: str = '127.0.0.1,localhost'
    APP_USE_TZ: bool = False
    APP_TIMEZONE: str = 'UTC'
    APP_JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    APP_DOCS_URL: Optional[str] = '/docs'

    # -----------------web server-----------------
    SERVER_NAME: str = ''
    SERVER_HOST: str = 'http://localhost'

    GUNICORN_HOST: str = '0.0.0.0'
    GUNICORN_PORT: str = '8000'
    WEB_CONCURRENCY: str = '4'
    GUNICORN_BIND_PATH: Optional[str] = None

    # -----------------end-----------------

    # -----------------middleware-----------------
    APP_MIDDLEWARE_ENABLE_BruteForceDefenderMiddleware: bool = False
    APP_MIDDLEWARE_ENABLE_IpProtectionMiddleware: bool = False
    APP_MIDDLEWARE_ENABLE_TrustedHostMiddleware: bool = False
    APP_MIDDLEWARE_ENABLE_CORSMiddleware: bool = True
    APP_MIDDLEWARE_ENABLE_SessionMiddleware: bool = False

    APP_MIDDLEWARE_TRUSTED_HOST: List[str] = ['localhost', '127.0.0.1']
    APP_MIDDLEWARE_LOCAL_IPS: List[str] = ["127.0.0.1", "localhost"]
    APP_MIDDLEWARE_ADMIN_IPS: List[str] = ['172.30.12.137', '172.30.12.138']

    APP_MIDDLEWARE_CORS_ALLOW_ORIGINS: List[str] = []
    APP_MIDDLEWARE_CORS_ALLOW_METHODS: List[str] = []
    APP_MIDDLEWARE_CORS_ALLOW_HEADERES: List[str] = []
    # -----------------end-----------------

    # -----------------database-----------------
    APP_DB_MONGO_ENABLED: bool = False
    APP_DB_MONGO_URI: Optional[str] = None
    APP_DB_MONGO_NAME: Optional[str] = None
    APP_DB_MONGO_USER: Optional[str] = None
    APP_DB_MONGO_PASSWORD: Optional[str] = None
    APP_DB_MONGO_HOST: Optional[str] = None
    APP_DB_MONGO_PORT: Optional[str] = None


    # -----------------end-----------------
    
    # -----------------Reids Start---------------
    
    REDIS_SERVER : Optional[str] = 'localhost'
    REDIS_PORT : Optional[str] = '6379'
    
    
    
    
    WS_SERVER_ENABLE_DEBUGGING: bool = True
    # ``'*'`` to allow all origins, or to ``[]`` to disable CORS handling, tested
    WS_SERVER_CORS_ORIGINS: Union[str, List] = "*"
    WS_SERVER_MOUNT_LOCATION: str = "/ws"
    WS_SERVER_SOCKETIO_PATH: str = "socket.io"
    WS_SERVER_KEEP_ALIVE: int = 120
    WS_SERVER_MAX_FILE_SIZE: int = 90 * (10**6)  # bytes  -> 10 Mb
    WS_SERVER_PING_TIMEOUT: int = 20  # s        -> 30 s
    WS_SERVER_PING_INTERVAL: int = 50  # s        -> 30 s

    
    # -----------------Reids End-----------------
    
    
    # -----------------Telegram-----------------
    APP_TELEGRAM_BOT_TOKEN: Optional[str] = None
    APP_TELEGRAM_NOTIFICATION_CHANNEL: Optional[str] = None
    APP_TELEGRAM_ERROR_CHANNEL: Optional[str] = None
    APP_TELEGRAM_ADMIN_ID: Optional[str] = None
    # -----------------end-----------------

basedir = os.getcwd()
env_file = os.path.join(basedir, 'etc', '.env')
with open(env_file, 'r') as f:
    result = f.readline()
    print(result)
settings = AppEnvConfig(_env_file=env_file)  # type: ignore

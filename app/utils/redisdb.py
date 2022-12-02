# -*- coding: utf-8 -*-
# flake8: noqa
import base64
import time
from typing import Any, List, Dict, Tuple
from pydantic import BaseModel
from datetime import datetime
from app.utils.signleton import SingletonClass
from app.configs import settings
import redis

# "172.27.230.25:54278
# username: admin
# password: admin
# db: exam"

class RedisClient(SingletonClass):
    def _singleton_init(self, **kwargs):
        self.client = None

    def _create_conn(self):
        self.client = redis.StrictRedis(host='172.27.230.25',
                                    port=54278,
                                    db=0,
                                    username='admin',
                                    password='admin',
                                    retry_on_timeout=True)
    
    async def get_client(self):
        if not self.client:
            self._create_conn()
        return self.client
    
redis_client  = RedisClient()
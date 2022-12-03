# -*- coding: utf-8 -*-
# flake8: noqa
import time, ujson
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
    
    def convert_result_redis_to_dict(self, data : dict):
        result = {}
        for k,v in data.items():
            result.update({
                k.decode() : v.decode()
            })
        return result
    
    def _create_conn(self):
        self.client = redis.StrictRedis(host='172.27.228.236',
                                    port=6379,
                                    db=0,
                                    password='02011993',
                                    retry_on_timeout=True)
    
    def get_client(self):
        if not self.client:
            self._create_conn()
            
    async def hget_key(self,name):
        if not self.client:
            self.get_client()
        return self.client.hgetall(name)
            
    async def hset_key(self, key, value, time=None):
        if not self.client:
            self.get_client()
        if time:
            data = {"count" : value, "time" : int(time)}
            return self.client.hset(name=key, mapping=data)
        
        data = {"count" : value}
        return self.client.hset(name=key, mapping=data)
    async def limmit_request(self, email):
        key = f"limit-request__change-profile___{email}"
        self.get_client()
        limit = await self.hget_key(key)
        if limit:
            result_limit = self.convert_result_redis_to_dict(limit)
        if not limit:
            await self.hset_key(key, 1, int(time.time()))
            return 1
        else:
            if (int(time.time()) - int(result_limit.get('time'))) < 1*60:
                await self.hset_key(key, int(result_limit.get("count")) +  1)
                return int(result_limit.get('count')) + 1
            else:
                await self.hset_key(key, 1, int(time.time()))
        return 1

redis_client  = RedisClient()
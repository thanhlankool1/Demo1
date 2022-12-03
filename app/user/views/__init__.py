from typing import List, Any
from pydantic import BaseModel
from functools import wraps
from ..schemas.user import Login
from app.utils.redisdb import RedisClient

class ErrorResponseException(Exception):
    def __init__(
        self,
        msg: str,
        success: bool = False,
        data: List[Any] = [],
  
    ):
        self.msg = msg
        self.success = success
        self.data = data

#response_model = 
class APIResponse(BaseModel):
    success: bool = False
    data: List[Any] = []
    msg : str =  ""  

async def get_limit(*args, **kwargs):
    if kwargs.get("current_user"):
        email = kwargs.get("current_user", {}).get("email")
        if not email:
            raise ErrorResponseException(msg="Token is not define")
        result = await RedisClient().limmit_request(email)
        if int(result) <= 30: # ignore
            return True
        else:
            return False
    raise ErrorResponseException(msg="Token is not define")

def limit_connect(
    func
):
    if func:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await get_limit(*args, **kwargs)
            if not result:
                raise ErrorResponseException(msg="Limit request")
            return await func(*args, **kwargs)
        return wrapper
import json, hashlib, uuid
from functools import wraps
from fastapi import Depends, APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse

from . import APIResponse

#import utils
from app.utils.celery import *
from app.utils.redisdb import redis_client
from app.utils.logger import logger
from app.utils.authentication import JwtAuthen, get_user_in_jwt

#import Schema
from app.user.schemas.user import UserRegister, Login, Verify

#import models
from app.user.models import UserInfo, Userprofile
router = APIRouter(tags=['Authentication'])


@router.post("/register", response_model=APIResponse)
async def register(data : UserRegister):
    new_user : UserInfo = await UserInfo.find_one({  # type: ignore
        "email" : data.email,
    })
    if new_user:
        return {
            "msg" : "User is exits"
        }
    
    new_user : UserInfo = UserInfo(
        username = data.email.split("@")[0],
        email = data.email,
        password = hashlib.md5(data.password.encode()).hexdigest())
    
    await new_user.commit()  # type: ignore
    
    if new_user:
        new_profile : Userprofile = Userprofile(
            user_id = new_user.id  # type: ignore
        )
        await new_profile.commit()  # type: ignore
        
    return {
        "data" : [{
            "username" : new_user.username,
            "email" : new_user.email,
            "id" : str(new_user.id),  # type: ignore
        }]
    }
    
@router.get('/whoami', response_model=APIResponse)
async def whoami(user : Login = Depends(get_user_in_jwt)):
    msg = 'Valid Token'
    if not user:
        msg = 'Invalid Token'
        
    return JSONResponse(
        content= {"msg" : msg}
    )
    
@router.post("/login", response_model=APIResponse)
async def login(data : Login):
    if not data:
        return {}
    
    is_user : UserInfo = await UserInfo.find_one({  # type: ignore
        "email" : data.email,
        "password" : hashlib.md5(data.password.encode()).hexdigest()
    })
    
    if not is_user:
        return {
            "msg" : "not found user"
        }
    
    return {
        "success" : True,
        "data" : [{
            "username" : data.email,
        "id" : str(is_user.id), # type: ignore
        "token" : JwtAuthen().encode({
            "email" : is_user.email,
            "password" : hashlib.md5(is_user.password.encode()).hexdigest()  # type: ignore
            })
        }]
    }

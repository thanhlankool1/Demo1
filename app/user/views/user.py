from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from typing import List, Any
from pydantic import BaseModel

from . import APIResponse, limit_connect

#import utils
from app.utils.celery import *
from app.utils.redisdb import redis_client
from app.utils.logger import logger
from app.utils.authentication import get_user_in_jwt

#import Schema
from app.user.schemas.user import (
    Login,
    InputAddProfile
)

#import models
from app.user.models import UserInfo, Userprofile
router = APIRouter(tags=['Authentication'])

@router.post('/get_profile', response_model=APIResponse)
async def get_profile(current_user : Login = Depends(get_user_in_jwt)):
    if not current_user:
        return {
            "msg" : "not ok"
        }
    user : UserInfo = await UserInfo.find_one({  # type: ignore
        "email" : current_user.get("email") # type: ignore
        })  
    if not user:
        return {}
    
    user_profile : Userprofile = await Userprofile.find_one({  # type: ignore
        "user_id" : user.id  # type: ignore
    })
    
    
    data = {
        "_id" : str(user.id),  # type: ignore
        "username" : user.username,
        "email" : user.username,
        "full_name" : user_profile.full_name,
        "address" : user_profile.address,
        "phone_number" : user_profile.phone_number
    }

    return {
        "data" : [data]
    }
    
@router.post('/change_profile', response_model=APIResponse)
@limit_connect
async def change_profile(data: InputAddProfile, current_user : Login = Depends(get_user_in_jwt)):
    if not current_user:
        return JSONResponse(
            content= {
                "success" : False,
                "msg" : "Invalid token"
                }
        )
    data_info : UserInfo = await UserInfo.find_one({"email" : current_user.get("email")})  # type: ignore
    if not data_info:
        return { "msg" : "user info"}
    profile : Userprofile  = await Userprofile.find_one({
        "user_id" : data_info.id
    })
    
    if not profile:
        return { "msg" : "profile"}
    
    profile["address"] = data.address
    profile["full_name"] = data.full_name
    profile["phone_number"] = data.phone_number
    await profile.commit()
    
    data = {
        "_id" : str(data_info.id),  # type: ignore
        "username" : data_info.username,
        "email" : data_info.username,
        "full_name" : profile.full_name,
        "address" : profile.address,
        "phone_number" : profile.phone_number
    }
    
    return {
        "success" : True,
        "data" : [data]
    }

@router.post('/delete_profile', response_model=APIResponse)
async def delete_profile(current_user : Login = Depends(get_user_in_jwt)):
    if not current_user:
        return JSONResponse(
            content= {"msg" : "Invalid token"}
        )
    user_info : UserInfo = await UserInfo.find_one({"email" : current_user.get("email")})  # type: ignore
    if not user_info:
        return {}
    user_profile : Userprofile = await Userprofile.find_one({"user_id" : user_info.id})# type: ignore
    if user_profile:
        await user_profile.delete()
    
    await user_info.delete()
    
    return {"success" : True}

@router.get("/task_send_noti", response_model=APIResponse)
async def task():
    datas = {
        "delay" : 5,
        "name" : "LanLT23"
    }
    first_task.apply_async(
        args = [datas],
        link=save_to_mongo.s()
    )
    return True
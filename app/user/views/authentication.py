from fastapi import Depends, APIRouter, File, UploadFile, Form
from app.user.models import UserInfo
import json
from app.utils import celery
from app.utils.redisdb import redis_client
from app.utils.logger import logger
router = APIRouter(tags=['Authentication'])


@router.get("/login")
async def login():
    new_user : UserInfo = UserInfo(
        username = "lanlt23",
        email = "lanlt23@fpt.com.vn"
    )
    client =await redis_client.get_client()
    print(client)
    await new_user.commit()  # type: ignore
    return {
        "username" : new_user.username,
        "email" : new_user.email,
        "id" : str(new_user.id)  # type: ignore
    }
    
@router.get("/task")
async def task():
    datas = {
        "delay" : 5,
        "name" : "LanLT23"
    }
    celery.first_task.apply_async(
        args = [datas],
        link=celery.save_to_mongo.s()
    )
    return {"ok" : "ok"}
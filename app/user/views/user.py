from fastapi import Depends, APIRouter, File, UploadFile, Form
from fastapi.responses import RedirectResponse
from app.user.models import UserInfo, Role
from app.user.schemas.user import UserRegister, Login, Verify
import json
from functools import wraps
from app.utils import celery
from app.utils.redisdb import redis_client
from app.utils.logger import logger
import hashlib, uuid
from app.utils.authentication import JwtAuthen
router = APIRouter(tags=['Authentication'])


role_permission = {
    "new" : [],
    "admin" : ['get_info']
}

def check_role(
        func,
        permission_name=[]):
    def decorator():
        @wraps(func)
        async def wrapper(*args, **kwargs):
            pass
            # check role mapping permision
        return True

@router.post("/register")
async def register(data : UserRegister):
    new_user : UserInfo = await UserInfo.find_one({  # type: ignore
        "username" : data.email,
    })
    
    if new_user:
        return False
    
    new_user : UserInfo = UserInfo(
        username = data.username,
        email = data.email,
        password = hashlib.md5(data.password.encode()).hexdigest())
    
    await new_user.commit()  # type: ignore
    return {
        "username" : new_user.username,
        "email" : new_user.email,
        "id" : str(new_user.id),  # type: ignore
        "token" : JwtAuthen().encode({
            "username" : new_user.username,
            "password" : hashlib.md5(data.password.encode()).hexdigest()
            })
    }
    
@router.post("/login")
async def login(data : Login):
    if not data:
        return
    
    new_user : UserInfo = await UserInfo.find_one({  # type: ignore
        "username" : data.username,
        "password" : hashlib.md5(data.password.encode()).hexdigest()
    })
    
    print(new_user)
    if not new_user:
        return False
    
    return {
        "username" : data.username,
        "id" : str(new_user.id),  # type: ignore
        "token" : JwtAuthen().encode({
            "username" : data.username,
            "password" : hashlib.md5(data.password.encode()).hexdigest()
            })
    }

@router.post('/get_info')
@check_role(
    func,
    
)
async def get_my_info(user : Verify):
    if not user.token:
        return False
    try:
        info = JwtAuthen().decode(user.token)
    except Exception as e:
        return False
    
    data_info : UserInfo = await UserInfo.find_one({"username" : info.get("username")})  # type: ignore
    if data_info.role_name == 'new':
        return False
    
    return {
        "email" : data_info.email,
        "username" : data_info.username,
    }

    
@router.get("/task_send_noti")
async def task():
    datas = {
        "delay" : 5,
        "name" : "LanLT23"
    }
    celery.first_task.apply_async(
        args = [datas],
        link=celery.save_to_mongo.s()
    )
    return True


@router.post("/create_role")
async def create_role(data :dict):
    if await Role.find_one({
        "role_name" : data.get("role_name")
    }):
        return False
    
    new_role : Role= Role(
        role_name=data.get('role_name'),
        desc=data.get('desc',"")
    )
    await new_role.commit()
    
    return True
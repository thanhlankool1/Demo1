from pydantic import BaseModel, validator
from typing import Optional

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str
    
class Verify(BaseModel):
    token: str
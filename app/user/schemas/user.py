from pydantic import BaseModel, validator
from typing import Optional

class UserRegister(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str
    
class Verify(BaseModel):
    token: str

class InputAddProfile(BaseModel):
    full_name : str
    phone_number : str
    address : Optional[str]
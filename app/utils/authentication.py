import time
import jwt
import hashlib, uuid
from fastapi.exceptions import HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme : OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl='/usr/get-token')


async def get_user_in_jwt(token : str = Depends(oauth2_scheme)):
      if token:
         return JwtAuthen().decode(token)

class JwtAuthen():
   def __init__(self):
      self.secret_key = "lanlt23"
   
   def decode(self, token : str):
      if not token:
         return
      try:
         return jwt.decode(token, self.secret_key, algorithms=['HS256'])
      except Exception as e:
         return False
      
   def encode(self, data : dict):
      if not data:
         return False
      
      if not data.get("email"):
         pass
      
      data.update({
         'exp': time.time() + 100000
      })
      return jwt.encode(data, self.secret_key , algorithm='HS256')

import time
import jwt
import hashlib, uuid

class JwtAuthen():
   def __init__(self):
      self.secret_key = "lanlt23"
   
   def decode(self, token : str):
      if not token:
         return
      return jwt.decode(token, self.secret_key, algorithms=['HS256'])
   
   def encode(self, data : dict):
      if not data:
         return False
      
      if not data.get("email"):
         pass
      
      data.update({
         'exp': time.time() + 300
      })
      return jwt.encode(data, self.secret_key , algorithm='HS256')

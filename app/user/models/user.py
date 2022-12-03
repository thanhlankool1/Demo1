from app.utils.mongodb import umongo_cnx
from umongo import EmbeddedDocument, fields, Document

@umongo_cnx.register
class UserInfo(Document):
    username = fields.StringField()
    email = fields.EmailField()
    password = fields.StringField()
    fullname = fields.StringField(allow_none=True)
    role_name = fields.StringField(default='new')
    
    class Meta:
        collection_name = "userinfo"
    
    
    
@umongo_cnx.register
class Role(Document):
    role_name = fields.StringField()
    desc = fields.StringField(allow_none=True)
    class Meta:
        collection_name = "Role"
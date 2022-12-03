from app.utils.mongodb import umongo_cnx
from umongo import EmbeddedDocument, fields, Document

@umongo_cnx.register
class UserInfo(Document):
    username = fields.StringField()
    email = fields.EmailField()
    password = fields.StringField()
    role_name = fields.StringField(default='new')
    
    class Meta:
        collection_name = "userinfo"
    
@umongo_cnx.register
class Userprofile(Document):
    user_id = fields.ObjectIdField(required=True)
    full_name = fields.StringField(allow_none=True)
    phone_number = fields.StringField(allow_none=True)
    address = fields.StringField(allow_none=True)

    class Meta:
        collection_name = "userprofile"
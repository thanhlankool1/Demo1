from app.utils.mongodb import umongo_cnx
from umongo import EmbeddedDocument, fields, Document

@umongo_cnx.register
class UserInfo(Document):
    username = fields.StringField()
    email = fields.EmailField()
    password = fields.StringField()
    fullname = fields.StringField(allow_none=True)
    
    class Meta:
        collection_name = "userinfo"
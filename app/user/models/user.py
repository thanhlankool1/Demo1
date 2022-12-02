from app.utils.mongodb import umongo_cnx
from umongo import EmbeddedDocument, fields, Document

@umongo_cnx.register
class UserInfo(Document):
    username = fields.StringField()
    email = fields.EmailField()
    
    class Meta:
        collection_name = "userinfo"
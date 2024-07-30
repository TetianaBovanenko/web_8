from mongoengine import Document, StringField, ReferenceField, ListField, connect

connect(host="YOUR_MONGODB_ATLAS_CONNECTION_STRING") #your own creds to be provided as data is sensitive

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=4)
    quote = StringField(required=True)

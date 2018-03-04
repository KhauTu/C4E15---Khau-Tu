from mongoengine import Document, StringField, IntField, BooleanField

# Create collection
class Customer(Document):
    name = StringField()
    gender = IntField() # 0: female, 1: male
    email = StringField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()

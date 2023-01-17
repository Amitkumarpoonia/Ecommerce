from tortoise.models import Model

from tortoise import fields

class User(Model):
    id=fields.IntField(pk=True)
    username=fields.CharField(max_length=20,unique=True)
    passward=fields.CharField(max_length=25)
    

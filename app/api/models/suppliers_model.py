import peewee
from app.api.utils.db import db



class Suppliers(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    doc_num = peewee.IntegerField()
    email = peewee.CharField(unique=True)
    address = peewee.CharField()
    phone = peewee.CharField()
    created_at = peewee.DateTimeField()
   


    class Meta:
        database = db       
        
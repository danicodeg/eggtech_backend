import peewee
from app.api.utils.db import db


class Product_Type(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    created_at = peewee.DateTimeField()

    class Meta:
        database = db       
        
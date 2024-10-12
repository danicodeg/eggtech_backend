import peewee
from app.api.utils.db import db



class ProductType(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    created_at = peewee.DateTimeField()



    class Meta:
        database = db       
        
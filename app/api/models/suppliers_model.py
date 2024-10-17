import peewee
from app.api.models.states_models import States
from app.api.utils.db import db


class Suppliers(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    doc_num = peewee.IntegerField()
    email = peewee.CharField(unique=True)
    address = peewee.CharField()
    phone = peewee.CharField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='suppliers')
   
    class Meta:
        database = db       
        
import peewee
from app.api.utils.db import db
from app.api.models.states_models import States

class Customers(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    doc_num = peewee.IntegerField()
    email = peewee.CharField(unique=True)
    address = peewee.CharField()
    phone = peewee.CharField()
    payment_method = peewee.CharField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='customers')


    class Meta:
        database = db       
        
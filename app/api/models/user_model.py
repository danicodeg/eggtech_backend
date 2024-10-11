import peewee

from app.api.utils.db import db
from app.api.models.states_models import States


class User(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    password = peewee.CharField()
    phone = peewee.CharField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='user', null=True)



    class Meta:
        database = db       
        
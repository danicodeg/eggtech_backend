import peewee

from app.api.utils.db import db
from app.api.models.states_models import States


class Shed(peewee.Model):

    id = peewee.IntegerField()
    name_shed = peewee.CharField()
    total_hens = peewee.IntegerField()
    update_at = peewee.DateTimeField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='shed')
  


    class Meta:
        database = db       
        
import peewee

from app.api.utils.db import db
from app.api.models.states_models import States


class Production(peewee.Model):

    id = peewee.IntegerField()
    quantity = peewee.IntegerField()
    shed = peewee.CharField()
    defective_eggs = peewee.IntegerField()
    cull_hens = peewee.IntegerField()
    production_date = peewee.DateTimeField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='production')
  


    class Meta:
        database = db       
        
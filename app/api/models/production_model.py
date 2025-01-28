import peewee

from app.api.utils.db import db
from app.api.models.states_models import States
from app.api.models.shed_model import Shed


class Production(peewee.Model):

    id = peewee.IntegerField()
    quantity = peewee.IntegerField()
    defective_eggs = peewee.IntegerField()
    cull_hens = peewee.IntegerField()
    production_date = peewee.DateTimeField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='production')
    shed_id = peewee.ForeignKeyField(Shed, backref='production')
  


    class Meta:
        database = db        
        
         
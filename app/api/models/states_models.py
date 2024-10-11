import peewee

from app.api.utils.db import db

class States(peewee.Model):
   id = peewee.AutoField()
   description_status = peewee.CharField()
   created_at = peewee.DateTimeField()

   class Meta:
       database = db
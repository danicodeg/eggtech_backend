import peewee

from app.api.utils.db import db



class BillType(peewee.Model):

    id = peewee.IntegerField()
    name_bill_type = peewee.CharField()
    created_at = peewee.DateTimeField()
    



    class Meta:
        database = db    
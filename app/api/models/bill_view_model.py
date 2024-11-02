import peewee


from app.api.utils.db import db


class BillView(peewee.Model):
    id = peewee.IntegerField()
    total = peewee.DecimalField()
    quantity = peewee.IntegerField()
    cliente= peewee.CharField()
    product= peewee.CharField()
    estado = peewee.CharField()

    class Meta:
        database = db 
        table_name = 'bill_view'
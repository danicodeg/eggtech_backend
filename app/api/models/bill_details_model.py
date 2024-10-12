import peewee

from app.api.models.bill_model import Bill
from app.api.models.products_model import Products
from app.api.utils.db import db


class BillDetails(peewee.Model):

    id = peewee.IntegerField()
    total_detail = peewee.DecimalField()
    created_at = peewee.DateTimeField()
    id_bill= peewee.ForeignKeyField(Bill, backref='billdetails', null=True )
    id_products = peewee.ForeignKeyField(Products, backref='billdetails', null=True )



    class Meta:
        database = db    
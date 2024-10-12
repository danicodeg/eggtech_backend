import peewee

from app.api.models.products_model import Products
from app.api.models.states_models import States
from app.api.utils.db import db


class Stock(peewee.Model):

    id = peewee.IntegerField()
    entry_products_date = peewee.DateField()
    product_exit_date = peewee.DateField()
    quantity = peewee.IntegerField()
    total = peewee.DecimalField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='stock')
    id_products = peewee.ForeignKeyField(Products, backref='stock', null=True )



    class Meta:
        database = db    
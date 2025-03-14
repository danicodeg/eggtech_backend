import peewee
from app.api.models.bill_type_model import BillType
from app.api.models.states_models import States
from app.api.utils.db import db
from app.api.models.customer_model import Customers
from app.api.models.products_model import Products

class Bill(peewee.Model):
    id = peewee.IntegerField()
    customers_id = peewee.ForeignKeyField(Customers, backref='bill')
    description = peewee.TextField()
    observations = peewee.TextField()
    status_id = peewee.ForeignKeyField(States, backref='bill')
    bill_type_id = peewee.ForeignKeyField(BillType, backref='bill_type_id')
    created_at = peewee.DateTimeField()

    class Meta:
        database = db

class BillDetails(peewee.Model):
    id = peewee.IntegerField()
    bill_id = peewee.ForeignKeyField(Bill, backref='details')
    products_id = peewee.ForeignKeyField(Products, backref='bill_details')
    quantity = peewee.IntegerField()
    unit_cost = peewee.DecimalField()
    total = peewee.DecimalField()

    class Meta:
        database = db
        table_name = 'bill_details'  # Especifica el nombre de la tabla en la base de datos
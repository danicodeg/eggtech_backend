import peewee
from app.api.models.product_type_model import ProductType
from app.api.models.suppliers_model import Suppliers
from app.api.utils.db import db
from app.api.models.states_models import States


class Products(peewee.Model):

    id = peewee.IntegerField()
    name = peewee.CharField()
    measuring_unit = peewee.CharField()
    expiration_date = peewee.DateField()
    unit_cost = peewee.DecimalField()
    created_at = peewee.DateTimeField()
    status_id = peewee.ForeignKeyField(States, backref='products')
    suppliers_id = peewee.ForeignKeyField(Suppliers, backref='products')
    product_type_id = peewee.ForeignKeyField(ProductType, backref='products')


    class Meta:
        database = db       
        
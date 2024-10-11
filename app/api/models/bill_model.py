import peewee

from app.api.models.customer_model import Customers
from app.api.utils.db import db
from app.api.models.states_models import States


class Bill(peewee.Model):

    id = peewee.IntegerField()
    bill_date = peewee.DateField()
    unit_cost = peewee.DecimalField()
    total = peewee.DecimalField()
    created_at = peewee.DateTimeField()
    id_customers = peewee.ForeignKeyField(Customers, backref='bill', null=True )
    status_id = peewee.ForeignKeyField(States, backref='bill', null=True)


    class Meta:
        database = db    
import peewee

from app.api.models.bill_type_model import BillType
from app.api.models.customer_model import Customers
from app.api.utils.db import db
from app.api.models.states_models import States


class Bill(peewee.Model):

    id = peewee.IntegerField()
    bill_date = peewee.DateField()
    total = peewee.DecimalField()
    created_at = peewee.DateTimeField()
    id_customers = peewee.ForeignKeyField(Customers, backref='bill', null=True )
    status_id = peewee.ForeignKeyField(States, backref='bill', null=True)
    id_bill_type = peewee.ForeignKeyField(BillType, backref='bill', null=True )



    class Meta:
        database = db    
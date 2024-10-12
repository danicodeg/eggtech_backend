
import datetime
from app.api.schema import customer_schema
from app.api.models.customer_model import Customers



def create_Customer(client: customer_schema.CustomerBase):

    customer=Customers(
        name=client.name,
        doc_num=client.doc_num,
        phone=client.phone,
        email=client.email,
        address=client.address,
        payment_method=client.payment_method,
        status_id =client.status_id,
        created_at=datetime.datetime.now())
    customer.save()

    return  {"message":"Saved", "status_code":200}


def get_one_customer(customer_id: customer_schema.CustomerBase):
    client = Customers.filter(Customers.id == customer_id).dicts().first()

    return client

def get_customers_all():

    clients = [customer for customer in Customers.select().dicts()]
    return clients


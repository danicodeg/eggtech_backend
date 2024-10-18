
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

    clients = [customer for customer in Customers.select().order_by(Customers.id.desc()).dicts()]
    return clients

def update_Customer(customer_id: int, client: customer_schema.CustomerBase):
 
    customer = Customers.get_or_none(Customers.id == customer_id)
    if not customer:
        return {"message": "Customer not found", "status_code": 404}

    
    customer.name = client.name
    customer.doc_num = client.doc_num
    customer.phone = client.phone
    customer.email = client.email
    customer.address = client.address
    customer.payment_method = client.payment_method
    customer.status_id = client.status_id
    customer.updated_at = datetime.datetime.now()

    customer.save()  # Guardar cambios

    return {"message": "Updated", "status_code": 200}
    
def delete_Customer(customer_id: int):
    
    
    customer = Customers.get_or_none(Customers.id == customer_id)
    if not customer:
        return {"message": "Customer not found", "status_code": 404}

    
    customer.delete_instance()

    return {"message": "Deleted", "status_code": 200}

    



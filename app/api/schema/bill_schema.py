# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class Product_Type(BaseModel):
    id_product_type: int
    name: str

class Customer(BaseModel):

    name: str
    doc_num: int
    phone: str
    email: str
    address: str
    payment_method: str
    status_id: int

class BillBase(BaseModel):

    total: int
    bill_date: datetime
    observation: str
    description: str
    status_id: int
    customers_id: int
    bill_type_id: int
    
    

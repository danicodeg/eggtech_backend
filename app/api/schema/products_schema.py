# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class ProductType(BaseModel):
    id_product_type: int
    name: str

class Suppliers(BaseModel):
    suppliers_id: int
    name: str
    doc_num: int
    email: str
    address: str
    phone: str
    status_id: int



class ProductsBase(BaseModel):

    name: str
    measuring_unit: str
    expiration_date: datetime
    unit_cost: int
    status_id: int
    suppliers_id: int
    product_type_id: int
    
    

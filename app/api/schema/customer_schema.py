# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class CustomerBase(BaseModel):

    name: str
    doc_num: int
    phone: str
    email: str
    address: str
    payment_method: str
    status_id: int
    
    

# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class SuppliersBase(BaseModel):

    name: str
    doc_num: int
    email: str
    address: str
    phone: str
    status_id: int
    
    

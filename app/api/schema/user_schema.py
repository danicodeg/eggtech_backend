# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class UserBase(BaseModel):

    name: str
    email: str
    password: str
    phone: str
    status_id: int
    
    

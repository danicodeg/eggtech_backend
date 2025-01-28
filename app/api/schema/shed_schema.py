# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class ShedBase(BaseModel):

    name_shed: str
    total_hens: int
    status_id: int
    
    

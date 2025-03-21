# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class Status(BaseModel):
    id_status: int
    description_status: str

class ProductionBase(BaseModel):

    quantity: int
    defective_eggs: int
    cull_hens: int
    production_date: datetime
    status_id: int
    shed_id: int
    
    

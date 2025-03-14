# schemas/invoice_schemas.py
from pydantic import BaseModel
from datetime import datetime

class BillBase(BaseModel):
    customers_id: int
    description: str
    observations: str
    status_id: int
    bill_type_id: int

class BillCreate(BillBase):
    pass

class Bill(BillBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class BillDetailBase(BaseModel):
    products_id: int
    quantity: int
    unit_cost: float
    total: float

class BillDetailCreate(BillDetailBase):
    pass

class BillDetail(BillDetailBase):
    id: int
    bill_id: int

    class Config:
        orm_mode = True
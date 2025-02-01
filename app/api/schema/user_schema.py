# Python
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    password: str
    status_id: Optional[int] = Field(default=1)

class UserResponse(UserBase):
    id: int
    created_at: datetime
    status_id: int

    class Config:
        from_attributes = True
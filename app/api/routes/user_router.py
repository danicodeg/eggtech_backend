from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import user_schema
from app.api.services.user import create_User, get_Users
from app.api.utils.db import get_db


router = APIRouter(prefix="/api")

@router.post(
     "/user/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(user: user_schema.UserBase = Body(...)):
     return create_User(user)



@router.get("/user/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_User():
    return get_Users()
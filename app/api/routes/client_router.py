from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import client_schema
from app.api.services.client import create_Client
from app.api.utils.db import get_db


router = APIRouter(prefix="/api")

@router.post(
     "/client/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     response_model=client_schema.ClientBase,
     dependencies=[Depends(get_db)]
 )
def create(client: client_schema.ClientBase = Body(...)):
     return create_Client(client)



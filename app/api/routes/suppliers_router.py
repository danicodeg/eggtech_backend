from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import suppliers_schema
from app.api.services.suppliers import create_suppliers, get_one_suppliers, get_suppliers_all
from app.api.utils.db import get_db



router = APIRouter(prefix="/api")

@router.post(
     "/suppliers/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(provider: suppliers_schema.SuppliersBase = Body(...)):
     return create_suppliers(provider)


@router.get("/suppliers/{suppliers_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_suppliers(suppliers_id: int):
    return get_one_suppliers(suppliers_id)


@router.get("/suppliers/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_supplier_all():
    return get_suppliers_all()


from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.utils.db import get_db

from app.api.services.dashboard import get_productions_type_all, get_products_type_all



router = APIRouter(prefix="/api")

@router.get("/dashboard/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_product_type_all():
    return get_products_type_all()

@router.get("/dashboard/production", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_production_type_all():
    return get_productions_type_all()
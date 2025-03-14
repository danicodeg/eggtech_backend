# app/api/routes/bill_router.py
from fastapi import APIRouter, Depends, Body
from fastapi import status  # type: ignore

from app.api.schema import bill_schema
from app.api.services.bill import create_bill, get_one_bill, get_bills_all, update_bill, delete_bill
from app.api.utils.db import get_db

router = APIRouter(prefix="/api")

@router.post(
    "/bills/",
    tags=["create"],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_db)]
)
def create(bill: bill_schema.BillCreate = Body(...), details: list[bill_schema.BillDetailCreate] = Body(...)):
    return create_bill(bill, details)

@router.get("/bills/{bill_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def get_bill(bill_id: int):
    return get_one_bill(bill_id)

@router.get("/bills/", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def get_bill_all():
    return get_bills_all()

@router.put("/bills/{bill_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def update_bill(bill_id: int, bill: bill_schema.BillCreate = Body(...)):
    return update_bill(bill_id, bill)

@router.delete("/bills/{bill_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def delete_bill(bill_id: int):
    return delete_bill(bill_id)
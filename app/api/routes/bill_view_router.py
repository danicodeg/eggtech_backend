from fastapi import APIRouter, Depends, Body, HTTPException, status
from app.api.schema import bill_schema
from app.api.services.bill_view import create_Bill, get_all_bills, get_all_bills_detail, get_bill_view_by_id, get_one_bills
from app.api.utils.db import get_db

router = APIRouter(prefix="/api")

#bill post

@router.post(
     "/bills/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(bill: bill_schema.BillBase = Body(...)):
     return create_Bill(bill)


@router.get(
    "/bills/",
    tags=["bills"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def get_all():
    return get_all_bills()

@router.get(
    "/bills/{bills_id}",
    tags=["bills"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def get_bill_by_id(bills_id: int):
    bill = get_one_bills(bills_id)
    if not bill:
        return {"message": "Bill not found", "status_code": 404}
    return bill

# view bill

@router.get(
    "/bill-view",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def get_all_bill_details():
    return get_all_bills_detail()

@router.get(
    "/bill-view/{bill_id}",
    tags=["bill-view"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def get_bill_view(bill_id: int):
    bill_view = get_bill_view_by_id(bill_id)
    if not bill_view:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill_view
from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import customer_schema
from app.api.services.customer import create_Customer, get_one_customer, get_customers_all, update_Customer, delete_Customer
from app.api.utils.db import get_db



router = APIRouter(prefix="/api")

@router.post(
     "/client/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(client: customer_schema.CustomerBase = Body(...)):
     return create_Customer(client)


@router.get("/client/{customer_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_customer(customer_id: int):
    return get_one_customer(customer_id)


@router.get("/client/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_customer_all():
    return get_customers_all()


@router.put("/client/{customer_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def update_customer(customer_id: int, client: customer_schema.CustomerBase = Body(...)):
    return update_Customer(customer_id, client)

@router.delete("/client/{customer_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def delete_customer(customer_id: int):
    return delete_Customer(customer_id)




from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import products_schema
from app.api.services.products import create_Products, get_one_Product, get_Products_all, update_Products, delete_Products
from app.api.utils.db import get_db



router = APIRouter(prefix="/api")

@router.post(
     "/products/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(products: products_schema.ProductsBase = Body(...)):
     return create_Products(products)


@router.get("/products/{products_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_product(products_id: int):
    return get_one_Product(products_id)


@router.get("/products/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_product_all():
    return get_Products_all()

@router.put("/products/{products_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def update_product(products_id: int, product: products_schema.ProductsBase = Body(...)):
    return update_Products(products_id, product)


@router.delete("/products/{products_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def delete_product(products_id: int):
    return delete_Products(products_id)



import datetime
from app.api.schema import products_schema
from app.api.models.products_model import Products



def create_Products(product: products_schema.ProductsBase):

    products=Products(
    name=product.name,
    measuring_unit=product.measuring_unit,
    unit_cost=product.unit_cost,
    expiration_date=product.expiration_date,
    status_id =product.status_id,
    suppliers_id= product.suppliers_id,
    product_type_id=product.product_type_id,
    created_at=datetime.datetime.now())
   
    
    products.save()

    return  {"message":"Saved", "status_code":200}


def get_one_Product(products_id: products_schema.ProductsBase):
    product = Products.filter(Products.id == products_id).dicts().first()

    return product

def get_Products_all():

    Product = [products for products in Products.select().order_by(Products.id.desc()).dicts()]
    return Product

def update_Products(products_id: int, productss: products_schema.ProductsBase):
 
    productt = Products.get_or_none(Products.id == products_id)
    if not productt:
        return {"message": "Product not found", "status_code": 404}

    
    productt.name = productss.name
    productt.measuring_unit = productss.measuring_unit
    productt.expiration_date = productss.expiration_date
    productt.unit_cost = productss.unit_cost
    productt.status_id = productss.status_id
    productt.suppliers_id = productss.suppliers_id
    productt.product_type_id = productss.product_type_id
    productt.updated_at = datetime.datetime.now()

    productt.save()  # Guardar cambios

    return {"message": "Updated", "status_code": 200}


def delete_Products(product_id: int):
    
    
    products = Products.get_or_none(Products.id == product_id)
    if not products:
        return {"message": "Product not found", "status_code": 404}

    
    products.delete_instance()

    return {"message": "Deleted", "status_code": 200}



import datetime
from app.api.schema import suppliers_schema
from app.api.models.suppliers_model import Suppliers



def create_suppliers(provider: suppliers_schema.SuppliersBase):

    suppliers=Suppliers(
        name=provider.name,
        doc_num=provider.doc_num,
        email=provider.email,
        address=provider.address,
        phone=provider.phone,
        status_id =provider.status_id,
        created_at=datetime.datetime.now())
    suppliers.save()

    return  {"message":"Saved", "status_code":200}


def get_one_suppliers(suppliers_id: suppliers_schema.SuppliersBase):
    provider = Suppliers.filter(Suppliers.id == suppliers_id).dicts().first()

    return provider

def get_suppliers_all():

    providers = [suppliers for suppliers in Suppliers.select().order_by(Suppliers.id.desc()).dicts()]
    return providers

def update_Supplier(suppliers_id: int, provider: suppliers_schema.SuppliersBase):
 
    supplier = Suppliers.get_or_none(Suppliers.id == suppliers_id)
    if not supplier:
        return {"message": "Supplier not found", "status_code": 404}

    
    supplier.name = provider.name
    supplier.doc_num = provider.doc_num
    supplier.phone = provider.phone
    supplier.email = provider.email
    supplier.address = provider.address
    supplier.status_id = provider.status_id
    supplier.updated_at = datetime.datetime.now()

    supplier.save()  # Guardar cambios

    return {"message": "Updated", "status_code": 200}


def delete_Supplier(suppliers_id: int):
    
    
    provider = Suppliers.get_or_none(Suppliers.id == suppliers_id)
    if not provider:
        return {"message": "Supplier not found", "status_code": 404}

    
    provider.delete_instance()

    return {"message": "Deleted", "status_code": 200}
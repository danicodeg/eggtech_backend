
import datetime
from app.api.schema import shed_schema
from app.api.models.shed_model import Shed



def create_shed(sheds: shed_schema.ShedBase):

    shed=Shed(
        
        name_shed=sheds.name_shed,
        total_hens=sheds.total_hens,
        update_at=datetime.datetime.now(),
        status_id =sheds.status_id,
        created_at=datetime.datetime.now())
    shed.save()

    return  {"message":"Saved", "status_code":200}


def get_one_shed(shed_id: shed_schema.ShedBase):
    sheds = Shed.filter(Shed.id == shed_id).dicts().first()

    return sheds

def get_shed_all():

    sheds = [shed for shed in Shed.select().order_by(Shed.id.desc()).dicts()]
    return sheds

def update_Shed(shed_id: int, sheds: shed_schema.ShedBase):
 
    shed = Shed.get_or_none(Shed.id == shed_id)
    if not shed:
        return {"message": "Supplier not found", "status_code": 404}

    
    shed.name_shed = sheds.name_shed
    shed.total_hens = sheds.total_hens
    shed.updated_at = datetime.datetime.now()
    shed.created_at = datetime.datetime.now()
    shed.status_id = sheds.status_id

    shed.save()  # Guardar cambios

    return {"message": "Updated", "status_code": 200}


def delete_Shed(shed_id: int):
    
    
    sheds = Shed.get_or_none(Shed.id == shed_id)
    if not sheds:
        return {"message": "Supplier not found", "status_code": 404}

    
    sheds.delete_instance()

    return {"message": "Deleted", "status_code": 200}


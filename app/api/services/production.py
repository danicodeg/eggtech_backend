
import datetime
from app.api.schema import production_schema
from app.api.models.production_model import Production



def create_production(productions: production_schema.ProductionBase):

    production=Production(
        quantity=productions.quantity,
        defective_eggs=productions.defective_eggs,
        cull_hens=productions.cull_hens,
        production_date=productions.production_date,
        status_id =productions.status_id,
        shed_id =productions.shed_id,
        created_at=datetime.datetime.now())
    production.save()

    return  {"message":"Saved", "status_code":200}


def get_one_production(production_id: production_schema.ProductionBase):
    productions = Production.filter(Production.id == production_id).dicts().first()

    return productions

def get_productions_all():

    productions = [production for production in Production.select().order_by(Production.id.desc()).dicts()]
    return productions

def update_Production(production_id: int, productions: production_schema.ProductionBase):
 
    production = Production.get_or_none(Production.id == production_id)
    if not production:
        return {"message": "Supplier not found", "status_code": 404}

    
    production.quantity = productions.quantity
    production.defective_eggs = productions.defective_eggs
    production.cull_hens = productions.cull_hens
    production.date = productions.production_date
    production.status_id = productions.status_id
    production.shed_id = productions.shed_id
    production.updated_at = datetime.datetime.now()

    production.save()  # Guardar cambios

    return {"message": "Updated", "status_code": 200}


def delete_Production(production_id: int):
    
    
    productions = Production.get_or_none(Production.id == production_id)
    if not productions:
        return {"message": "Supplier not found", "status_code": 404}

    
    productions.delete_instance()

    return {"message": "Deleted", "status_code": 200}


from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import production_schema
from app.api.services.production import create_production, get_one_production, get_productions_all, update_Production, delete_Production
from app.api.utils.db import get_db



router = APIRouter(prefix="/api")

@router.post(
     "/production/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(productions: production_schema.ProductionBase = Body(...)):
     print("post production:: ", production_schema)
     return create_production(productions)


@router.get("/production/{production_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_production(production_id: int):
    return get_one_production(production_id)


@router.get("/production/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_production_all():
    return get_productions_all()

@router.put("/production/{production_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def update_production(production_id: int, productions: production_schema.ProductionBase = Body(...)):
    return update_Production(production_id, productions)


@router.delete("/production/{production_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def delete_production(production_id: int):
    return delete_Production(production_id)




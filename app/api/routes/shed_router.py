from fastapi import APIRouter, Depends, Body
from fastapi import status # type: ignore

from app.api.schema import shed_schema
from app.api.services.shed import create_shed, get_one_shed, get_shed_all, update_Shed, delete_Shed
from app.api.utils.db import get_db



router = APIRouter(prefix="/api")

@router.post(
     "/shed/",
     tags=["create"],
     status_code=status.HTTP_201_CREATED,
     dependencies=[Depends(get_db)]
)
def create(sheds: shed_schema.ShedBase = Body(...)):
     return create_shed(sheds)


@router.get("/shed/{shed_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_shed(shed_id: int):
    return get_one_shed(shed_id)


@router.get("/shed/", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def get_sheds_all():
    return get_shed_all()

@router.put("/shed/{shed_id}", status_code=status.HTTP_200_OK, dependencies=[Depends(get_db)])
def update_shed(shed_id: int, sheds: shed_schema.ShedBase = Body(...)):
    return update_Shed(shed_id, sheds)


@router.delete("/shed/{shed_id}", status_code=status.HTTP_200_OK,dependencies=[Depends(get_db)])
def delete_shed(shed_id: int):
    return delete_Shed(shed_id)




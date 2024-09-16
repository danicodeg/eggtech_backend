
import datetime
from fastapi import HTTPException, status
from app.api.schema import client_schema
from app.api.models.client_model import Client_Test


def create_Client(client: client_schema.ClientBase):

    rec1=Client_Test(
        nombre=client.nombre,
        telefono=client.telefono,
        correo=client.correo,
        direccion=client.direccion, 
        fecha=datetime.datetime.now())
    rec1.save()

    return  {"message":"Saved", "status_code":200}


def get_clients(client: client_schema.ClientBase, is_done: bool = None):

    if(is_done is None):
        clients = Client_Test.filter(Client_Test.id == client.id).order_by(Client_Test.fecha.desc())
    else:
        clients = Client_Test.filter((Client_Test.id == client.id) & (Client_Test.is_done == is_done)).order_by(Client_Test.fecha.desc())

    list_tasks = []
    for task in clients:
        list_tasks.append(
            client_schema.ClientBase(
                nombre = task.nombre,
                telefono = task.telefono,
                correo = task.correo,
                direccion = task.direccion
            )
        )

    return list_tasks

def get_client(client_id: int, client: client_schema.ClientBase):
    task = Client_Test.filter((Client_Test.user_id == client.id)).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return client_schema.ClientBase(
        nombre = task.nombre,
        telefono = task.telefono,
        correo = task.correo,
        direccion = task.direccion
    )
# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class ClientBase(BaseModel):

    nombre: str
    telefono: str
    correo: str
    direccion: str
    

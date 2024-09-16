import peewee

from app.api.utils.db import db

class Client_Test(peewee.Model):

    nombre = peewee.CharField()
    telefono = peewee.CharField()
    correo = peewee.CharField(unique=True)
    direccion = peewee.CharField()
    fecha = peewee.DateTimeField()

    class Meta:
        database = db

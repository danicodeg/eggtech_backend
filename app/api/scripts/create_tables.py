from app.api.models.client_model import Client_Test

from app.api.utils.db import db

def create_tables():
    with db:
        db.create_tables([Client_Test])

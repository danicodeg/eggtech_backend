from app.api.models.customer_model import Customers

from app.api.utils.db import db

def create_tables():
    with db:
        db.create_tables([Customers])

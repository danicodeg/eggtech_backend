# app/api/services/bill.py
from app.api.utils.db import db
from app.api.models.bill_model import Bill, BillDetails
from app.api.schema.bill_schema import BillCreate, BillDetailCreate

def create_bill(bill: BillCreate, details: list[BillDetailCreate]):
    with db.atomic():  # Usa db.atomic() para manejar transacciones
        # Crear la factura
        bill_db = Bill.create(
            customers_id=bill.customers_id,  # Cambia customer_id a customers_id
            description=bill.description,
            observations=bill.observations,
            status_id=bill.status_id,
            bill_type_id=bill.bill_type_id  # Campo opcional
        )

        # Crear los detalles de la factura
        for detail in details:
            BillDetails.create(
                bill_id=bill_db.id,
                products_id=detail.products_id,
                quantity=detail.quantity,
                unit_cost=detail.unit_cost,
                total=detail.total
            )

        return bill_db

def get_one_bill(bill_id: int):
    return Bill.get_or_none(Bill.id == bill_id)

def get_bills_all():
    return list(Bill.select())

def update_bill(bill_id: int, bill: BillCreate):
    bill_db = Bill.get_or_none(Bill.id == bill_id)
    if bill_db:
        for key, value in bill.dict().items():
            setattr(bill_db, key, value)
        bill_db.save()
        return bill_db
    return None

def delete_bill(bill_id: int):
    bill_db = Bill.get_or_none(Bill.id == bill_id)
    if bill_db:
        bill_db.delete_instance()
        return True
    return False
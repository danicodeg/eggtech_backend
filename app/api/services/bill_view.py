import datetime
from app.api.models.bill_model import Bill
from app.api.models.bill_view_model import BillView
from app.api.schema import bill_schema  


#este es el de bill

def create_Bill(bills: bill_schema.BillBase):

    bill=Bill(
        bill_date=bills.bill_date,
        total=bills.total,
        customers_id=bills.id_customers,
        bill_type_id=bills.bill_type_id,
        status_id =bills.status_id,
        created_at=datetime.datetime.now())
    bill.save()

    return  {"message":"Saved", "status_code":200}


   
def get_all_bills():
       
    return list(Bill.select().dicts())



# este es el de detalles/vista
def get_all_bills_detail():
       
    return list(BillView.select().dicts())

def get_bill_view_by_id(bill_id: int):
    bill_details = BillView.filter(BillView.id == bill_id).dicts().first()

    return bill_details



  
   





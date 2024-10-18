
import datetime
from app.api.schema import user_schema
from app.api.models.user_model import User



def create_User(user: user_schema.UserBase):

    user=User(
        name=user.name,
        phone=user.phone,
        email=user.email,
        password=user.password,
        status_id =user.status_id,
        created_at=datetime.datetime.now())
    user.save()

    return  {"message":"Saved", "status_code":200}



def get_Users():

    users = [us for us in User.select().dicts()]
    return users

def update_User(user_id: int, users: user_schema.UserBase):
 
    userss = User.get_or_none(User.id == user_id)
    if not users:
        return {"message": "User not found", "status_code": 404}

    
    userss.name = users.name
    userss.phone = users.phone
    userss.email = users.email
    userss.password = users.password
    userss.status_id = users.status_id
    userss.updated_at = datetime.datetime.now()

    userss.save()  # Guardar cambios

    return {"message": "Updated", "status_code": 200}

def delete_User(user_id: int):
    
    
    userss = User.get_or_none(User.id == user_id)
    if not userss:
        return {"message": "Supplier not found", "status_code": 404}

    
    userss.delete_instance()

    return {"message": "Deleted", "status_code": 200}
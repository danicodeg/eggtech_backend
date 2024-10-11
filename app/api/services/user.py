
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


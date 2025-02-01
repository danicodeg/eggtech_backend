from passlib.context import CryptContext
import datetime
from app.api.models.user_model import User
from app.api.schema.user_schema import UserCreate, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(email: str):
    return User.get_or_none(User.email == email)

def create_user(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    user_db = User.create (
        name=user.name,
        email=user.email,
        password=hashed_password,
        phone=user.phone,
        created_at= datetime.datetime.now(),
        status_id=user.status_id or 1
    )
    return user_db

def authenticate_user(email: str, password: str):
    user = User.get_or_none(User.email == email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

import secrets as _secrets
import sqlalchemy.orm as _orm
import passlib.hash as _hash

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from ..database import database as _database
from ..model import model as _model
from ..schema import schema as _schema

def create_database():
    return _database.BASE.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_email(email:str, db:_orm.Session):
    return db.query(_model.User).filter(_model.User.email == email).first()

# generate a random salt using secrets
SECRET_KEY = _secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def create_new_user(user:_schema.UserCreate, db:_orm.Session):
    # store the user data in the sql's model(table) format, also encrypt the password
    new_user = _model.User(
        email=user.email,
        hash_password = _hash.bcrypt.hash(user.hashed_password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

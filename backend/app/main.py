import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from .service import service as _service
from .schema import schema as  _schema

app = _fastapi.FastAPI()

@app.post(path="/users")
async def create_user(user:_schema.UserCreate, db:_orm.Session = _fastapi.Depends(_service.get_db)):
    # check if the email is already present in the database or not
    new_user = await _service.get_user_by_email(
        email = user.email,
        db = db
    )
    if new_user:
        raise _fastapi.HTTPException(
            status_code=_fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Email already in use. Try to do login instead."
        )
    return await _service.create_new_user(
        user=user,
        db = db
    )
    
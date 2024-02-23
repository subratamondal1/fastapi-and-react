"""Database Models (SQL Table): Represent the structure of 'data' 
in your database (e.g., users, posts, comments)"""

import datetime as _dt

import pydantic as _pydantic

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import passlib.hash as _hash

import database as _database

class PostSchema(_pydantic.BaseModel):
    id: int = _pydantic.Field(default=None)
    title: str = _pydantic.Field(default=None)
    content: str = _pydantic.Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Some title, for sampling",
                "content": "Some content"
            }
        }
class UserSchema(_pydantic.BaseModel):
    firstname:str = _pydantic.Field(default=None)
    lastname:str = _pydantic.Field(default=None)
    email: _pydantic.EmailStr = _pydantic.Field(default=None)
    password: str = _pydantic.Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "firstname":"Subrata",
                "lastname": "Mondal",
                "email":"subrata@gmail.com",
                "password":"@1234"
            }
        }

class UserLoginSchema(_pydantic.BaseModel):
    email: _pydantic.EmailStr = _pydantic.Field(default=None)
    password: str = _pydantic.Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email":"subrata@gmail.com",
                "password":"@1234"
            }
        }

class User(_database.Base):
    """User's Database Table"""

    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)

    leads = _orm.relationship("Lead", back_populates="owner")

    def verify_password(self, password: str):
        """Password Verification"""
        return _hash.bcrypt.verify(password, self.hashed_password)


class Lead(_database.Base):
    """Lead's Database Table"""

    __tablename__ = "leads"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    firstname = _sql.Column(_sql.String, index=True)
    lastname = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    company = _sql.Column(_sql.String, index=True, default="")
    note = _sql.Column(_sql.String, default="")
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship("User", back_populates="leads")

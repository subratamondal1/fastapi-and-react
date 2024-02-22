"""Schemas: Define how 'data' is presented in API requests and responses, 
often based on models."""

import datetime as _dt

import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    """Base schema for User data, including email."""

    email: str


class UserCreate(_UserBase):
    """Schema for creating a new User.
    Contains the email address and a password hash.
    """

    hashed_password: str

    class Config:
        """Enable automatic data conversion between models and schemas"""

        orm_mode = True


class User(_UserBase):
    """Schema for representing a User.
    Inherits from `_UserBase` and includes the User ID.
    """

    id: int

    class Config:
        """Enable automatic data conversion between models and schemas"""

        orm_mode = True


class _Lead(_pydantic.BaseModel):
    """Base schema for Lead data, including name, email, and company."""

    firstname: str
    lastname: str
    email: str
    company: str
    note: str


class LeadCreate(_Lead):
    """Schema for creating a new Lead.
    Inherits from `_Lead` and doesn't require any additional fields.
    """


class Lead(_Lead):
    """Schema for representing a Lead.
    Inherits from `_Lead` and includes additional fields like ID, owner ID, and timestamps.
    """

    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        """Enable automatic data conversion between models and schemas"""

        orm_mode = True

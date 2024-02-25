"""MODEL for SQL TABLES"""

from sqlalchemy import Column, Integer, String
from database import BASE

class Books(BASE):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)
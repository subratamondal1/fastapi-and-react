from statistics import mode
from typing_extensions import final
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.BASE.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating:int = Field(gt=-1, lt=101)

BOOKS = []

@app.get(path="/")
def read_api(db:Session = Depends(get_db)):
    return db.query(models.Books).all()

@app.post(path="/")
def create_book(book:Book, db:Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.rating = book.rating

    db.add(book_model) # add data to db
    db.commit()
    return book

@app.put(path="/{book_id}")
def update_book(book_id:int, book:Book, db:Session = Depends(get_db)):
    # extracting book with given id from the db
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not book_model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID:{book_id}: Does not exist"
        )
    # update data of the book with specific id
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()
    return book
    
@app.delete(path="/{book_id}")
def delete_book(book_id:int, db:Session = Depends(get_db)):
    # extracting book with given id from the db
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not book_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID:{book_id}: Does not exist"
        )
    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()


    

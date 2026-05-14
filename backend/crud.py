from sqlalchemy.orm import Session
import models
import schemas

# BOOK CRUD

def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# BORROWER CRUD

def get_borrowers(db: Session):
    return db.query(models.Borrower).all()

def create_borrower(db: Session, borrower: schemas.BorrowerCreate):
    db_borrower = models.Borrower(**borrower.dict())
    db.add(db_borrower)
    db.commit()
    db.refresh(db_borrower)
    return db_borrower
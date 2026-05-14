from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud
import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_borrowers(db: Session = Depends(get_db)):
    return crud.get_borrowers(db)

@router.post("/")
def create_borrower(
    borrower: schemas.BorrowerCreate,
    db: Session = Depends(get_db)
):
    return crud.create_borrower(db, borrower)
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    category: str
    isbn: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int
    availability_status: str

    class Config:
        from_attributes = True


class BorrowerBase(BaseModel):
    borrower_name: str
    email: str
    phone: str

class BorrowerCreate(BorrowerBase):
    pass

class Borrower(BorrowerBase):
    borrower_id: int

    class Config:
        from_attributes = True


class Transaction(BaseModel):
    transaction_id: int
    book_id: int
    borrower_id: int
    borrow_date: datetime
    return_date: Optional[datetime]

    class Config:
        from_attributes = True
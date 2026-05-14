from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine

from routers import books, borrowers, transactions

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    books.router,
    prefix="/books",
    tags=["Books"]
)

app.include_router(
    borrowers.router,
    prefix="/borrowers",
    tags=["Borrowers"]
)

app.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["Transactions"]
)

@app.get("/")
def root():
    return {"message": "Library Management Backend Running"}
from fastapi import FastAPI

from backend import crud

from . import models
from .database import SessionLocal, engine

db = SessionLocal()
# crud.create_entry(
#     db,
#     betrag=12.99,
#     typ="ausgabe",
#     kategorie="Essen",
#     beschreibung="Pizza",
#     datum="2025-07-24",
# )
# crud.update_entry(db, id=1, betrag=20)

# models.Base.metadata.create_all(bind=engine)
# crud.delete_all_entries(db=db)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastFinance API läuft!"}

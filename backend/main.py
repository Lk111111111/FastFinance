from fastapi import FastAPI

from backend import crud

from . import models
from .database import SessionLocal, engine

db = SessionLocal()
crud.create_entry(
    db,
    betrag=12.99,
    typ="ausgabe",
    kategorie="Essen",
    beschreibung="Pizza",
    datum="2025-07-24",
)
crud.update_entry(db, id=1, betrag=20)


i = crud.get_all_entries(db=db)
for all_entries in i:
    crud.delete_entry(db, all_entries.id)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastFinance API läuft!"}

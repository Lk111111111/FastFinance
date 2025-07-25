from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from backend import crud, models, schemas
from backend.database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastFinance API läuft!"}


@app.post("/entries")
def entry_create(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(
        db=db,
        betrag=entry.betrag,
        typ=entry.typ,
        kategorie=entry.kategorie,
        beschreibung=entry.beschreibung,
        datum=entry.datum,
    )


@app.get("/entries")  # Einträge abrufen
def entry_function():
    pass


@app.get("/entries/{id}")  # Eintrag anzeigen
def entry_function():
    pass


@app.put("/entries/{id}")  # Eintrag aktualisieren
def entry_function():
    pass


@app.delete("/entries/{id}")  # Eintrag löschen
def entry_function():
    pass


@app.get("/summary")  # Summe Einnahmen/Ausgaben
def entry_function():
    pass


@app.get("/summary/month")  # Monatsübersicht
def entry_function():
    pass

from fastapi import Depends, FastAPI, Path
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


@app.delete("/entries/{id}")  # Eintrag löschen
def delete_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    deleted = crud.delete_entry(db=db, id=id)
    if deleted is None:
        return {"message": f"Kein Eintrag mit ID {id} gefunden."}
    return {"message": f"Eintrag mit ID {id} wurde gelöscht."}


@app.get("/entries", response_model=list[schemas.EntryRead])  # Einträge abrufen
def entry_function(db: Session = Depends(get_db)):
    return crud.get_all_entries(db=db)


@app.get("/entries/{id}")  # Eintrag anzeigen
def entry_function():
    pass


@app.put("/entries/{id}")  # Eintrag aktualisieren
def entry_function():
    pass


@app.get("/summary")  # Summe Einnahmen/Ausgaben
def entry_function():
    pass


@app.get("/summary/month")  # Monatsübersicht
def entry_function():
    pass

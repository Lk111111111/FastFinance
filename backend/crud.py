from sqlalchemy.orm import Session
from . import models
import datetime

# crud = create, read, update, delete


def create_entry(
    db: Session,
    betrag: float,
    typ: str,
    kategorie: str,
    beschreibung: str = "",
    datum: str = None,
):
    # creates new entry in table entry autoamtically assigns primary key
    if datum is None:
        datum = datetime.date.today()
    else:
        datum = datetime.date.fromisoformat(datum)
    entry = models.Entry(
        betrag=betrag,
        typ=typ,
        kategorie=kategorie,
        beschreibung=beschreibung,
        datum=datum,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def delete_entry(db: Session, id: int):
    # deletes entry with primary key id
    entry = db.query(models.Entry).filter(models.Entry.id == id).first()
    if entry is None:
        return None
    db.delete(entry)
    db.commit()
    return entry


def update_entry(
    db: Session,
    id: int,
    betrag: float = None,
    typ: str = None,
    kategorie: str = None,
    beschreibung: str = None,
    datum: str = None,
):
    # updates the entry table based on given parameters
    entry = db.query(models.Entry).filter(models.Entry.id == id).first()
    if entry is None:
        return None
    update_data = {
        "betrag": betrag,
        "typ": typ,
        "kategorie": kategorie,
        "beschreibung": beschreibung,
        "datum": datum,
    }
    for key, value in update_data.items():
        if value is not None:
            setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return entry


def get_all_entries(db: Session):
    return db.query(models.Entry).all()

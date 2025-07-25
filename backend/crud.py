import datetime

from sqlalchemy.orm import Session

from . import models
from .database import SessionLocal, engine


def create_entry(
    db: Session,
    betrag: float,
    typ: str,
    kategorie: str,
    beschreibung: str = "",
    datum: str = None,
):
    """
    Erstelle einen neuen Eintrag in der Datenbank.

    Args:
        db (Session): Aktive SQLAlchemy-Datenbank-Session.
        betrag (float): Betrag des Eintrags (z. B. 12.50).
        typ (str): Art des Eintrags, z. B. "einnahme" oder "ausgabe".
        kategorie (str): Kategorie des Eintrags, z. B. "Lebensmittel".
        beschreibung (str, optional): Freitextbeschreibung.
        datum (str, optional): Datum im Format 'YYYY-MM-DD'. Wenn nicht angegeben, wird heute verwendet.

    Returns:
        models.Entry: Das neu erstellte Entry-Objekt.
    """
    if isinstance(datum, str):
        datum = datetime.date.fromisoformat(datum)
    elif datum is None:
        datum = datetime.date.today()
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


def get_single_entry(db: Session, id: int):
    return db.query(models.Entry).filter(models.Entry.id == id).first()


def delete_entry(db: Session, id: int):
    """
    Löscht einen Eintrag anhand seiner ID.

    Args:
        db (Session): Aktive Datenbankverbindung.
        id (int): Primärschlüssel (ID) des zu löschenden Eintrags.

    Returns:
        models.Entry | None: Das gelöschte Entry-Objekt, oder None wenn nicht gefunden.
    """
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
    """
    Aktualisiert einen vorhandenen Eintrag mit übergebenen Werten.

    Nur Felder, die nicht None sind, werden aktualisiert.

    Args:
        db (Session): Aktive Datenbankverbindung.
        id (int): ID des zu aktualisierenden Eintrags.
        betrag (float, optional): Neuer Betrag.
        typ (str, optional): Neuer Typ ("einnahme" oder "ausgabe").
        kategorie (str, optional): Neue Kategorie.
        beschreibung (str, optional): Neue Beschreibung.
        datum (str, optional): Neues Datum im Format 'YYYY-MM-DD'.

    Returns:
        models.Entry | None: Der aktualisierte Eintrag oder None, wenn nicht gefunden.
    """
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
    """
    Gibt alle vorhandenen Einträge aus der Datenbank zurück.

    Args:
        db (Session): Aktive Datenbankverbindung.

    Returns:
        list[models.Entry]: Liste aller gespeicherten Einträge.
    """
    return db.query(models.Entry).all()


def delete_all_entries(db: Session):
    """
    Löscht alle Einträge aus der Datenbank.

    Args:
        db (Session): Aktive Datenbankverbindung.
    """
    all_entries = get_all_entries(db)
    for entry in all_entries:
        delete_entry(db, entry.id)

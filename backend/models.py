import datetime

from sqlalchemy import Column, Date, Float, Integer, String

from .database import Base


class Entry(Base):
    """Entry table in der Sqllite Datenbank soll alle transaktionen darstellen

    Args:
        Base (_type_): Zentralregister erzeugt tabellen aus klassen
    """

    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    betrag = Column(Float, nullable=False)
    typ = Column(String, nullable=False)  # "einnahme" oder "ausgabe"
    kategorie = Column(String, nullable=False)
    beschreibung = Column(String, nullable=True)
    datum = Column(Date, default=datetime.date.today)

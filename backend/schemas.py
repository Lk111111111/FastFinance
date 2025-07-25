import datetime
from typing import Literal

from pydantic import BaseModel


class EntryCreate(BaseModel):
    betrag: float
    typ: Literal["einnahme", "ausgabe"]
    kategorie: Literal[
        "Lebensmittel",
        "Transport",
        "Fast Food",
        "Gehalt",
        "Freizeit",
        "Monatliche Fixkosten",
    ]
    beschreibung: str
    datum: datetime.date


class EntryRead(EntryCreate):
    "read entry kategorie hier string weil vorher durchgeschossen mit literal"

    id: int
    kategorie: str

    class Config:
        from_attributes = True  # fastapi orm modelle werden zu json

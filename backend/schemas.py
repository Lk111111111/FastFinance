import datetime
from typing import Literal, Optional
from unittest.mock import Base

from pydantic import BaseModel
from sqlalchemy import literal


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


class EntryUpdate(BaseModel):
    betrag: Optional[float]
    typ: Optional[str]
    kategorie: Optional[str]
    beschreibung: Optional[str]
    datum: Optional[datetime.date]

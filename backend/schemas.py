import datetime

from pydantic import BaseModel


class EntryCreate(BaseModel):
    betrag: float
    typ: str
    kategorie: str
    beschreibung: str
    datum: datetime.date


class EntryRead(EntryCreate):
    id: int

    class Config:
        from_attributes = True  # fastapi orm modelle werden zu json

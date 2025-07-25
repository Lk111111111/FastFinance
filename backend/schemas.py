import datetime

from pydantic import BaseModel


class EntryCreate(BaseModel):
    betrag: float
    typ: str
    kategorie: str
    beschreibung: str
    datum: str


class EntryRead(EntryCreate):
    id: int

    class Config:
        orm_mode = True  # fastapi orm modelle werden zu json

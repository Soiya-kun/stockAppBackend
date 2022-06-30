import datetime

from pydantic import BaseModel


class ScNoteBase(BaseModel):
    sc: str
    note: str
    b_date: datetime.date


class ScNoteCreated(ScNoteBase):
    pass


class ScNoteInDBBase(ScNoteBase):
    class Config:
        orm_mode = True


class ScNote(ScNoteInDBBase):
    pass

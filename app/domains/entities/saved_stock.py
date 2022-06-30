import datetime
from typing import Optional

from pydantic import BaseModel


class SavedStockBase(BaseModel):
    sc: str
    b_date: datetime.date
    note: Optional[str]


class SavedStockCreated(SavedStockBase):
    pass


class SavedStockInDB(SavedStockBase):
    id: int

    class Config:
        orm_mode = True


class SavedStock(SavedStockInDB):
    pass

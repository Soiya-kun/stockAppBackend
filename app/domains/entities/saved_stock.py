import datetime

from pydantic import BaseModel


class SavedStockBase(BaseModel):
    sc: str
    b_date: datetime.date


class SavedStockCreated(SavedStockBase):
    pass


class SavedStockInDB(SavedStockBase):
    id: int

    class Config:
        orm_mode = True


class SavedStock(SavedStockInDB):
    pass

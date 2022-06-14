from datetime import date

from pydantic import BaseModel


class StockSplitBase(BaseModel):
    sc: str
    split_date: date
    split_ratio: float


class StockSplitCreated(StockSplitBase):
    pass


class StockSplitInDBBase(StockSplitBase):
    id: int

    class Config:
        orm_mode = True


class StockSplit(StockSplitInDBBase):
    pass

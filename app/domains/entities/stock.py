import datetime

from pydantic import BaseModel


class StockBase(BaseModel):
    sc: str
    name: str
    market: str
    industry: str
    b_date: datetime.date
    opened_price: float
    high_price: float
    low_price: float
    closed_price: float
    volume: float
    transaction_price: float
    market_capitalization: float
    low_limit: float
    high_limit: float


class StockCreated(StockBase):
    pass


class StockInDBBase(StockBase):
    id: int

    class Config:
        orm_mode = True


class Stock(StockInDBBase):
    pass

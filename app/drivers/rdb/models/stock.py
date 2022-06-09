from sqlalchemy import Column, Integer, String, Date, Float

from app.drivers.rdb.base import Base


class Stock(Base):

    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    sc = Column(String(128), index=True)
    name = Column(String(128), index=True)
    market = Column(String(128), index=True)
    industry = Column(String(128), index=True)
    b_date = Column(Date, index=True)
    opened_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    closed_price = Column(Float)
    volume = Column(Float)
    transaction_price = Column(Float)
    market_capitalization = Column(Float)
    low_limit = Column(Float)
    high_limit = Column(Float)

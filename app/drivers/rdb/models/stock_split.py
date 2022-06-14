from sqlalchemy import Column, Integer, String, Date, Float

from app.drivers.rdb.base import Base


class StockSplit(Base):

    __tablename__ = "stock_splits"

    id = Column(Integer, primary_key=True, index=True)
    sc = Column(String(128), index=True)
    split_date = Column(Date, index=True)
    split_ratio = Column(Float)

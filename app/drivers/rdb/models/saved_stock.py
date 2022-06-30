from sqlalchemy import Column, Integer, String, Date, Text

from app.drivers.rdb.base import Base


class SavedStock(Base):

    __tablename__ = "saved_stocks"

    # TODO scとb_dateでUnique
    id = Column(Integer, primary_key=True, index=True)
    sc = Column(String(128), index=True)
    b_date = Column(Date, index=True)
    note = Column(Text)

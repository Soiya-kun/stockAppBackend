from sqlalchemy import Column, String, Text, DateTime, Date
from sqlalchemy.sql.functions import current_timestamp

from app.drivers.rdb.base import Base


class ScNote(Base):

    __tablename__ = "sc_notes"

    sc = Column(String(128), primary_key=True, index=True)
    created_at = Column(
        DateTime, primary_key=True, nullable=False, server_default=current_timestamp()
    )
    note = Column(Text)
    b_date = Column(Date, index=True)

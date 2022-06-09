from sqlalchemy import Column, Integer, String

from app.drivers.rdb.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=False, unique=True)
    hashed_password = Column(String(1024), nullable=False)

from sqlalchemy import Column, Integer, String

from .base import Base


class Shelf(Base):
    __tablename__ = "shelves"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)

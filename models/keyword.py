from sqlalchemy import Column, Integer, String

from .base import Base


class Keyword(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)

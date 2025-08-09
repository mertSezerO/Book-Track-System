from sqlalchemy import Column, Integer, String

from .base import Base


class Keyword(Base):
    keyword_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)

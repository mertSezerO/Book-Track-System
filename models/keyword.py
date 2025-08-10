from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .book_keywords import book_keywords


class Keyword(Base):
    __tablename__ = "keywords"
    keyword_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)

    books = relationship("Book", secondary=book_keywords, back_populates="keywords")

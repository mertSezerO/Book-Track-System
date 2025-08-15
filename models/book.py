from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base
from .book_keywords import book_keywords


class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)

    shelf_id = Column(Integer, ForeignKey("shelves.shelf_id"))
    shelf = relationship("Shelf", back_populates="books")
    keywords = relationship("Keyword", secondary=book_keywords, back_populates="books")
    notes = relationship("Note", back_populates="book")

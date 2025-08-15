from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from .base import Base


class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)

    book_id = Column(Integer, ForeignKey("books.book_id"))
    book = relationship("Book", back_populates="notes")

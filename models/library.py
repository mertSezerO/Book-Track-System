from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from .base import Base


class Library(Base):
    __tablename__ = "libraries"
    library_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)

    shelves = relationship("Shelf", back_populates="library")

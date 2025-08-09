from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Shelf(Base):
    __tablename__ = "shelves"
    shelf_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True, index=True, nullable=False)
    library_id = Column(Integer, ForeignKey("shelves.library_id"))
    library = relationship("Library", back_populates="shelves")

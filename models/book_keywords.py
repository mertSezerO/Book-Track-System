from sqlalchemy import Column, Integer, Table, ForeignKey
from .base import Base

book_keywords = Table(
    "book_keywords",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.book_id")),
    Column("keyword_id", Integer, ForeignKey("keywords.keyword_id")),
)

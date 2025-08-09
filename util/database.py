from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine("sqlite:///iskenderiye.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)


def commit_changes():
    try:
        session.commit()
        print("Changes added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")

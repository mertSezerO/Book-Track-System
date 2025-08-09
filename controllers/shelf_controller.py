from models import Shelf, Book
from util import session, commit_changes


class ShelfController:

    @staticmethod
    def create_shelf(name: str):
        new_shelf = Shelf(name=name)
        session.add(new_shelf)
        commit_changes()

    @staticmethod
    def get_shelf_by_id(shelf_id: int):
        return session.query(Shelf).get(shelf_id)

    @staticmethod
    def get_shelf_by_name(shelf_name: str):
        return session.query(Shelf).filter_by(name=shelf_name).first()

    @staticmethod
    def find_shelf_books_by_id(shelf_id: str):
        return session.query(Book).join(Shelf).filter_by(shelf_id=shelf_id).all()

    @staticmethod
    def find_shelf_books_by_name(shelf_name: str):
        return session.query(Book).join(Shelf).filter(Shelf.name == shelf_name).all()

    @staticmethod
    def update_shelf_name(shelf_id: int, new_name: str):
        session.query(Shelf).filter_by(shelf_id=shelf_id).update({"name": new_name})
        commit_changes()

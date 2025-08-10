from models import Shelf, Book
from util import session, commit_changes


class ShelfController:

    @staticmethod
    def create_shelf(name: str, library_id: int):
        is_shelf_exist = session.query(Shelf).filter_by(name=name).first()
        if is_shelf_exist:
            raise NameError("Shelf already exists!")
        new_shelf = Shelf(name=name, library_id=library_id)
        session.add(new_shelf)
        commit_changes()

    @staticmethod
    def get_shelves():
        return session.query(Shelf).all()

    @staticmethod
    def get_shelf_by_id(shelf_id: int):
        return session.query(Shelf).get(shelf_id)

    @staticmethod
    def get_shelf_by_name(shelf_name: str):
        return session.query(Shelf).filter_by(name=shelf_name).first()

    @staticmethod
    def find_shelf_books_by_id(shelf_id: str):
        return session.query(Book).join(Book.shelf).filter_by(shelf_id=shelf_id).all()

    @staticmethod
    def gather_library_shelves_by_id(library_id: int):
        return session.query(Shelf).filter_by(library_id=library_id).all()

    @staticmethod
    def gather_library_shelves_by_name(library_name: int):
        return session.query(Shelf).filter_by(library_name=library_name).all()

    @staticmethod
    def find_shelf_books_by_name(shelf_name: str):
        return (
            session.query(Book).join(Book.shelf).filter(Shelf.name == shelf_name).all()
        )

    @staticmethod
    def update_shelf_name(shelf_id: int, new_name: str):
        session.query(Shelf).filter_by(shelf_id=shelf_id).update({"name": new_name})
        commit_changes()

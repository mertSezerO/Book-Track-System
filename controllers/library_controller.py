from models import Shelf, Book, Library
from util import session, commit_changes


class LibraryController:

    @staticmethod
    def create_library(name: str):
        is_library_exist = session.query(Library).filter_by(name=name).first()
        if is_library_exist:
            raise NameError("Library already exists!")
        new_library = Library(name=name)
        session.add(new_library)
        commit_changes()

    @staticmethod
    def get_library_by_id(library_id: int):
        return session.query(Library).get(library_id)

    @staticmethod
    def get_library_by_name(library_name: str):
        return session.query(Library).filter_by(name=library_name).first()

    @staticmethod
    def find_library_books_by_id(library_id: str):
        return (
            session.query(Book)
            .join(Book.shelf)
            .join(Shelf.library)
            .filter_by(library_id=library_id)
            .all()
        )

    @staticmethod
    def find_library_books_by_name(library_name: str):
        return (
            session.query(Book)
            .join(Book.shelf)
            .join(Shelf.library)
            .filter(Library.name == library_name)
            .all()
        )

    @staticmethod
    def gather_library_shelves_by_id(library_id: int):
        return session.query(Shelf).join(Library).filter_by(library_id=library_id).all()

    @staticmethod
    def gather_library_shelves_by_name(library_name: int):
        return (
            session.query(Shelf)
            .join(Library)
            .filter_by(library_name=library_name)
            .all()
        )

    @staticmethod
    def update_library_name(library_id: int, new_name: str):
        session.query(Library).filter_by(library_id=library_id).update(
            {"name": new_name}
        )
        commit_changes()

from models import Shelf, Book
from util import session, commit_changes, Logger
from util.common import DBNotification, LogData


class ShelfController:

    @staticmethod
    def create_shelf(logger, name: str, library_id: int) -> DBNotification:
        try:
            is_shelf_exist = session.query(Shelf).filter_by(name=name).first()
            if is_shelf_exist:
                raise NameError("Shelf already exists!")
            new_shelf = Shelf(name=name, library_id=library_id)
            session.add(new_shelf)
            commit_changes()

            result = DBNotification(success=True, message="Shelf Created Successfully!", resource=new_shelf)
            logger.log(LogData(
                message="Shelf created successfully! \nWith Fields => Shelf: name={name} library_id={id}",
                source="controller",
                level="info",
                kwargs={"name": name, "id": library_id}
            ))

        except Exception as e:
            result = DBNotification(success=False, message=str(e))
            logger.log(LogData(
                message="Error on library creation! Error Message: {} \nWith Fields => Library: name={name}",
                source="controller",
                level="error",
                args=(str(e) ,),
                kwargs={"name": name}
            ))

        finally:
            return result


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
    def gather_library_shelves_by_id(logger, library_id: int):
        try:
            shelves = session.query(Shelf).filter_by(library_id=library_id).all()
            logger.log(LogData(
                message="Shelves fetched successfully!",
                source="controller",
                level="info"
            ))
            return shelves

        except Exception as e:
            logger.log(LogData(
                message="Error on shelves fetch! Error Message: {} ",
                source="controller",
                args=(str(e) ,),
                level="error"
            ))

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

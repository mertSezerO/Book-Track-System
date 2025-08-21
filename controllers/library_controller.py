from models import Shelf, Book, Library
from util import DatabaseConnector
from util.common import DBNotification, LogData


class LibraryController:

    @staticmethod
    def create_library(logger, name: str) -> DBNotification:
        try:
            is_library_exist = DatabaseConnector.session.query(Library).filter_by(name=name).first()
            if is_library_exist:
                raise NameError("Library already exists!")
            new_library = Library(name=name)
            DatabaseConnector.session.add(new_library)
            DatabaseConnector.commit_changes(logger)

            result = DBNotification(success=True, message="Library Added Successfully!", resource=new_library)
            logger.log(LogData(
                message="Library created successfully! \nWith Fields => Library: name={name}",
                source="controller",
                level="info",
                kwargs={"name": name}
            ))
            return result
        
        except Exception as e:
            result = DBNotification(success=False, message=str(e))
            logger.log(LogData(
                message="Error on library creation! Error Message: {} \nWith Fields => Library: name={name}",
                source="controller",
                level="error",
                args=(str(e) ,),
                kwargs={"name": name}
            ))
            return result

    @staticmethod
    def get_libraries(logger):
        try:
            libraries = DatabaseConnector.session.query(Library).all()
            logger.log(LogData(
                message="Libraries fetched successfully!",
                source="controller",
                level="info"
            ))
            return libraries
        
        except Exception as e:
            logger.log(LogData(
                message="Error on library fetch! Error Message: {} ",
                source="controller",
                args=(str(e) ,),
                level="error"
            ))

    @staticmethod
    def get_library_by_id(library_id: int):
        return DatabaseConnector.session.query(Library).get(library_id)

    @staticmethod
    def get_library_by_name(library_name: str):
        return DatabaseConnector.session.query(Library).filter_by(name=library_name).first()

    @staticmethod
    def find_library_books_by_id(library_id: str):
        return (
            DatabaseConnector.session.query(Book)
            .join(Book.shelf)
            .join(Shelf.library)
            .filter_by(library_id=library_id)
            .all()
        )

    @staticmethod
    def find_library_books_by_name(library_name: str):
        return (
            DatabaseConnector.session.query(Book)
            .join(Book.shelf)
            .join(Shelf.library)
            .filter(Library.name == library_name)
            .all()
        )

    @staticmethod
    def update_library_name(logger, library_id: int, new_name: str):
        DatabaseConnector.session.query(Library).filter_by(library_id=library_id).update(
            {"name": new_name}
        )
        DatabaseConnector.commit_changes(logger)

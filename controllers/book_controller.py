from sqlalchemy import and_

from models import Shelf, Book, Keyword, Library
from util import session, commit_changes, Logger
from util.common import TableData, DBNotification, LogData


class BookController:
    logger = Logger()

    @staticmethod
    def add_book(
        logger, name: str, author: str, category: str, translator: str, shelf_id: int, keywords: list[str]
    ) -> DBNotification:
        try:
            shelf = session.query(Shelf).get(shelf_id)
            if not shelf:
                raise ReferenceError("Incorrect shelf ID!")
            
            is_book_exist = session.query(Book).filter_by(name=name).first()
            if is_book_exist:
                raise NameError("The book already exist!")

            keyword_objs = []
            for keyword in keywords:
                keyword_obj = session.query(Keyword).filter_by(name=keyword).first()
                if not keyword_obj:
                    keyword_obj = Keyword(name=keyword)
                    logger.log(LogData(
                        message="Keyword created successfully! \nWith Fields => Keyword: name={name} For => Book: {book_name}",
                        source="controller",
                        level="info",
                        kwargs={"name":keyword, "book_name": name}
                    ))
                    session.add(keyword_obj)
                keyword_objs.append(keyword_obj)

            new_book = Book(
                name=name,
                author=author,
                category=category,
                translator=translator,
                shelf=shelf,
                keywords=keyword_objs,
            )
            session.add(new_book)

            result = DBNotification(success=True, message="Book Added Successfully!", resource=new_book)
            logger.log(LogData(
                message="Book created successfully! \nWith Fields => Book: name={name} author={author} category={category} shelf={shelf}",
                source="controller",
                level="info",
                kwargs={"name": name, "author": author, "category": category, "shelf": shelf_id}
            ))
        
        except Exception as e:
            result = DBNotification(success=False, message=str(e))
            logger.log(LogData(
                message="Error on book creation! Error Message: {} \nWith Fields => Book: name={name} author={author} category={category} shelf={shelf}",
                source="controller",
                level="error",
                args=(str(e) ,),
                kwargs={"name": name, "author": author, "category": category, "shelf": shelf_id}
            ))

        finally:
            commit_changes()
            return result

    @staticmethod
    def get_book_by_name(logger, book_name: str):
        try:
            book = session.query(Book).filter_by(name=book_name).first()
            logger.log(LogData(
                message="Book fetched successfully! \nFor Query => Book: name={name}",
                source="controller",
                level="info",
                kwargs={"name": book_name}
            ))
            return book
        except Exception as e:
            logger.log(LogData(
                message="Error on book creation! Error Message: {} \nFor Query => Book: name={name}}",
                source="controller",
                level="error",
                args=(str(e) ,),
                kwargs={"name": book_name}
            ))

    @staticmethod
    def get_book_by_id(book_id: int):
        return session.query(Book).get(book_id)

    @staticmethod
    def get_books_by_author(author: str):
        return session.query(Book).filter_by(author=author).all()

    @staticmethod
    def get_books_by_keyword(keyword: str):
        return session.query(Book).join(Keyword).filter(Keyword.name == keyword).all()

    @staticmethod
    def update_book_name(book_id: int, new_name: str):
        session.query(Book).filter_by(book_id=book_id).update({"name": new_name})
        commit_changes()

    @staticmethod
    def check_column_name(name: str):
        columns = Book.__table__.columns
        for col in columns:
            if col.name == name:
                return True
            
        return False

    @staticmethod
    def search_books_by_criteria(logger, criteria_dict: dict = None) -> TableData:
        try:
            if criteria_dict:
                filters = []
                for field, value in criteria_dict.items():
                    column = getattr(Book, field, None)
                    if column is not None:
                        filters.append(column.ilike(f"%{value}%"))

                if not filters:
                    return []
                
                results = session.query(Book).filter(and_(*filters)).join(Shelf).join(Library).all() 
            
            else:
                results = session.query(Book).join(Shelf).join(Library).all()
            
            logger.log(LogData(
                message="Books fetched successfully! \nReturn Size:{size} For Query => Book: query={query}",
                source="controller",
                level="info",
                kwargs={"size": len(results), "query": criteria_dict}
            ))
            return BookController.__convert_to_table_data(logger, results)
        
        except Exception as e:
            pass
    
    @staticmethod
    def __convert_to_table_data(logger, data: list[Book]) -> TableData:
        columns = ["Book ID", "Category", "Book Name", "Author", "Translator", "Library Name", "Shelf Name"]
        data_list = []

        for instance in data:
            data_tuple = (instance.book_id, instance.category, instance.name, instance.author, instance.translator, instance.shelf.library.name, instance.shelf.name)
            data_list.append(data_tuple)
        
        logger.log(LogData(
                message="Table data created successfully!",
                source="controller",
                level="debug"
            ))
        return TableData(columns=columns, data_list=data_list)
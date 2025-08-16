from sqlalchemy import and_

from models import Shelf, Book, Keyword, Library
from util import session, commit_changes, TableData


class BookController:

    @staticmethod
    def add_book(
        name: str, author: str, category: str, translator: str, shelf_id: int, keywords: list[str]
    ):
        try:
            shelf = session.query(Shelf).get(shelf_id)
            if not shelf:
                raise ReferenceError("Incorrect shelf ID!")

            keyword_objs = []
            for keyword in keywords:
                keyword_obj = session.query(Keyword).filter_by(name=keyword).first()
                if not keyword_obj:
                    keyword_obj = Keyword(name=keyword)
                    session.add(keyword_obj)
                keyword_objs.append(keyword_obj)

            is_book_exist = session.query(Book).filter_by(name=name).first()
            if is_book_exist:
                raise NameError("The book already exist!")

            new_book = Book(
                name=name,
                author=author,
                category=category,
                translator=translator,
                shelf=shelf,
                keywords=keyword_objs,
            )
            print("Book Added!")
            session.add(new_book)
        except:
            pass

        finally:
            print("Committed!")
            commit_changes()

    @staticmethod
    def get_book_by_name(book_name: str):
        return session.query(Book).filter_by(name=book_name).first()

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
    def search_books_by_criteria(criteria_dict: dict = None) -> TableData:
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
        return BookController.__convert_to_table_data(results)
    
    @staticmethod
    def __convert_to_table_data(data: list[Book]) -> TableData:
        columns = ["Book ID", "Category", "Book Name", "Author", "Translator", "Library Name", "Shelf Name"]
        data_list = []

        for instance in data:
            data_tuple = (instance.book_id, instance.category, instance.name, instance.author, instance.translator, instance.shelf.library.name, instance.shelf.name)
            data_list.append(data_tuple)
        
        return TableData(columns=columns, data_list=data_list)
from models import Shelf, Book, Keyword
from util import session, commit_changes


class BookController:

    @staticmethod
    def add_book(name: str, author: str, shelf_id: int, keywords: list[str]):
        try:
            shelf = session.query(Shelf).get(shelf_id)
            if not shelf:
                raise ReferenceError("Incorrect shelf ID!")

            keyword_objs = []
            for keyword in keywords:
                keyword_obj = session.query(Keyword).filter_by(name=keyword).first()
                if not keyword_obj:
                    keyword_obj = Keyword(keyword)
                    session.add(keyword_obj)
                keyword_objs.append(keyword_obj)

            is_book_exist = session.query(Book).filter_by(name=name).first()
            if is_book_exist:
                raise NameError("The book already exist!")

            new_book = Book(
                name=name, author=author, shelf=shelf, keywords=keyword_objs
            )
            session.add(new_book)
        except:
            pass

        finally:
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

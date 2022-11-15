from .db import DB


class Book:
    def __init__(self):
        self.db = DB.connect()

    def get_book_by_id(self, id):
        books = self.db.get_books()
        for book in books:
            if book["bookID"] == id:
                return book

    def update_description(self, id, desc):
        book = self.get_book_by_id(id)
        book["description"] = desc
        return book

    def update_rating(self, id, rate):
        book = self.get_book_by_id(id)
        book["average_rating"] = rate
        return book

    def list_books_by_author(self, auth):
        result = []
        for book in self.db.get_books():
            if book.get("authors") == auth:
                result.append(book)
        return result

    def list_books_by_rating(self, rate, rate_1):
        result = []
        for book in self.db.get_books():
            if float(book.get("average_rating")) in range(rate, rate_1):
                result.append(book)
        return result

    def list_books_by_language(self, lang):
        return list(filter(lambda book: book.get("language_code") == lang, self.db.get_books()))
        # result = []
        # for book in self.db.get_books():
        #     if book.get("language_code") == lang:
        #         result.append(book)
        # return result

    def list_books(self, shift, limit):
        return self.db.get_books()[shift:limit]

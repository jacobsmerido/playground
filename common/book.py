from .db import DB


class Book:
    def __init__(self):
        self.db = DB.connect()

    def get_book_by_id(cls):
        pass

    def update_description(self):
        self.db.save()

    def update_rating(self):
        pass

    def list_books_by_author(self):
        pass

    def list_books_by_rating(self):
        pass

    def list_books_by_language(self, lang):
        return list(filter(lambda book: book.get("language_code") == lang, self.db.get_books()))
        # result = []
        # for book in self.db.get_books():
        #     if book.get("language_code") == lang:
        #         result.append(book)
        # return result

    def list_books(self, shift, limit):
        return self.db.get_books()[shift:limit]
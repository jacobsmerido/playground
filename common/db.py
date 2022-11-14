import csv


class DB:
    def __init__(self, connections):
        self.connections = connections

    @classmethod
    def connect(cls):
        with open("./db/books.csv", "r", encoding="utf8", newline="") as file:
            books = list(csv.DictReader(file, delimiter=","))

        return cls({"books": books})

    def get_resource(self, resource):
        return self.connections[resource]

    def get_books(self):
        return self.get_resource("books")

    def save(self):
        books_keys = self.connections["books"][0].keys()
        with open("./db/books.csv", "w", encoding="utf8", newline="") as books_file:
            writer = csv.DictWriter(books_file, books_keys)
            writer.writeheader()
            writer.writerows(self.connections["books"])

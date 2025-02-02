from domain.entities.book import Book

class BookRepository:
    def __init__(self, client):
        self.client = client

    def add_book(self, book: Book, embedding: list):
        self.client.data_object.create(
            data_object={
                "title": book.title,
                "author": book.author,
                "description": book.description,
            },
            class_name="Book",
            vector=embedding,
        )
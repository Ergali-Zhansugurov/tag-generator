from typing import List
from domain.entities.book import Book
from domain.repositories.book_repository import BookRepository

class FindSimilarBooksUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, query: str, top_n: int = 3) -> List[Book]:
        return self.book_repository.find_similar_books(query, top_n)
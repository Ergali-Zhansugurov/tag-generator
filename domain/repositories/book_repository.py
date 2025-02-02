from abc import ABC, abstractmethod
from typing import List
from domain.entities.book import Book

class BookRepository(ABC):
    @abstractmethod
    def find_similar_books(self, query: str, top_n: int = 3) -> List[Book]:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass
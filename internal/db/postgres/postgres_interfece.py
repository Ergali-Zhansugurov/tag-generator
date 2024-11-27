from abc import ABC, abstractmethod

class TagRepositoryInterface(ABC):
    @abstractmethod
    def save_tags(self, tags: list[str]):
        """Сохраняет теги в базу данных"""
        pass

    @abstractmethod
    def save_book_tags(self, book_id: int, tags: list[str]):
        """Сохраняет связь книги с тегами"""
        pass
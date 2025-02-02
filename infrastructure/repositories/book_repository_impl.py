from domain.repositories.book_repository import BookRepository
from domain.entities.book import Book
from sentence_transformers import SentenceTransformer
import numpy as np

class BookRepositoryImpl(BookRepository):
    def __init__(self, faiss_storage, model: SentenceTransformer, books: List[Book]):
        self.faiss_storage = faiss_storage
        self.model = model
        self.books = books

    def find_similar_books(self, query: str, top_n: int = 3) -> List[Book]:
        query_embedding = self.model.encode([query])
        indices = self.faiss_storage.search(np.array(query_embedding, dtype=np.float32), top_n)
        return [self.books[i] for i in indices[0]]

    def get_all_books(self) -> List[Book]:
        return self.books
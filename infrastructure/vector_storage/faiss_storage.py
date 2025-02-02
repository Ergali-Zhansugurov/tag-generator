import faiss
import numpy as np

class FaissStorage:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embeddings(self, embeddings: np.ndarray):
        self.index.add(embeddings)

    def search(self, query_embedding: np.ndarray, top_n: int) -> np.ndarray:
        distances, indices = self.index.search(query_embedding, top_n)
        return indices
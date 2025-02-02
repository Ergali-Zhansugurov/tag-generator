from fastapi import FastAPI
from application.use_cases.find_similar_books import FindSimilarBooksUseCase
from infrastructure.repositories.book_repository_impl import BookRepositoryImpl
from infrastructure.vector_storage.faiss_storage import FaissStorage
from sentence_transformers import SentenceTransformer
from application.use_cases.classify_text import ClassifyTextUseCase
from infrastructure.ml_models.text_classifier import TextClassifier
from fastapi.responses import JSONResponse


app = FastAPI()
# Инициализация классификатора
classifier = TextClassifier(model_name="your-model-name")
classify_text_use_case = ClassifyTextUseCase(classifier)

@app.get("/search")
async def search(query: str):
    # Асинхронный поиск
    results = await search_books(query)
    return JSONResponse(results)

@app.post("/classify")
def classify(text: str):
    tags = classify_text_use_case.execute(text)
    return {"tags": tags}
# Инициализация зависимостей
model = SentenceTransformer("all-MiniLM-L6-v2")
faiss_storage = FaissStorage(dimension=384)
books = [...]  # Загрузите книги сюда
book_repository = BookRepositoryImpl(faiss_storage, model, books)
find_similar_books_use_case = FindSimilarBooksUseCase(book_repository)

@app.post("/search")
def search(query: str):
    books = find_similar_books_use_case.execute(query)
    return {"results": books}
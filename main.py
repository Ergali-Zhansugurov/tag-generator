from sentence_transformers import SentenceTransformer
import numpy as np

# Загружаем модель для работы с текстами
model = SentenceTransformer("all-MiniLM-L6-v2")

# База книг и их отзывов
books = {
    "Война и мир – Л.Н. Толстой": [
        "Глубокий роман о жизни и войне.",
        "Сложно, но интересно.",
        "Персонажи будто живые."
    ],
    "Гарри Поттер и философский камень – Дж.К. Роулинг": [
        "Волшебная история для всех возрастов.",
        "Легко читается, затягивает.",
        "Настоящее приключение!"
    ],
    "Братья Карамазовы – Ф.М. Достоевский": [
        "Сложные темы, глубина человеческой природы, философские размышления о вере, морали и судьбе.",
        "Достоевский гениально показывает внутренние конфликты людей."
    ],
    "451 градус по Фаренгейту – Рэй Брэдбери": [
        "Дистопия, предупреждающая об опасностях цензуры и равнодушия общества.",
        "Хотя роман написан давно, он не теряет актуальности."
    ],
    "Преступление и наказание – Ф.М. Достоевский": [
        "Очень глубокая книга о терзаниях души и моральном выборе.",
        "Заставляет задуматься о природе преступления и искупления.",
        "Местами тяжёлая, но после прочтения долго не отпускает."
    ]
}


# Функция для подбора нескольких книг по отзывам пользователя
def recommend_books(user_reviews, top_n=3):
    user_vector = model.encode(user_reviews)
    scores = []

    for book, reviews in books.items():
        book_vector = model.encode(reviews)
        score = np.mean(np.dot(user_vector, book_vector.T))  # Среднее сходство
        scores.append((book, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [book for book, _ in scores[:top_n]]


# Пример ввода от пользователя
user_reviews = [
    "Мне нравится глубокий смысл и философия книги.",
    "История должна быть сложной и затрагивать моральные вопросы.",
    "Важно, чтобы были интересные персонажи и конфликты."
]

recommended_books = recommend_books(user_reviews)
print("📖 Рекомендуемые книги:")
for book in recommended_books:
    print(f"- {book}")

# Главная функция
if __name__ == "__main__":
    recommended = recommended_books
from presentation.api.main import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
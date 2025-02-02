from transformers import pipeline

# Загружаем модель для сентимент-анализа
sentiment_analyzer = pipeline("sentiment-analysis")

def filter_reviews(reviews):
    meaningful_reviews = []
    for review in reviews:
        # Фильтрация по длине
        if len(review.split()) > 3:
            # Анализ сентимента
            sentiment = sentiment_analyzer(review)[0]
            if sentiment['label'] == 'POSITIVE' or sentiment['label'] == 'NEGATIVE':
                meaningful_reviews.append(review)
    return meaningful_reviews

# Пример использования
for book in books:
    book["reviews"] = filter_reviews(book["reviews"])
from transformers import pipeline

class ReviewFilter:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def filter(self, reviews: list) -> list:
        meaningful_reviews = []
        for review in reviews:
            if len(review.split()) > 3:  # Фильтрация по длине
                sentiment = self.sentiment_analyzer(review)[0]
                if sentiment["label"] in ["POSITIVE", "NEGATIVE"]:  # Фильтрация по сентименту
                    meaningful_reviews.append(review)
        return meaningful_reviews

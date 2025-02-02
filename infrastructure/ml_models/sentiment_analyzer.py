from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline("sentiment-analysis")

    def analyze(self, text: str) -> str:
        result = self.model(text)[0]
        return result["label"]
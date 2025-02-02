from transformers import pipeline

class TextClassifier:
    def __init__(self, model_name: str):
        self.model = pipeline("text-classification", model=model_name)

    def predict(self, text: str):
        return self.model(text)
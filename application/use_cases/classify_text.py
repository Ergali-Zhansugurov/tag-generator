from typing import List
from domain.entities.category import Category, Tag

class ClassifyTextUseCase:
    def __init__(self, classifier):
        self.classifier = classifier

    def execute(self, text: str) -> List[Tag]:
        # Используем классификатор для получения тегов
        predictions = self.classifier.predict(text)
        return [Tag(name=pred["label"], confidence=pred["score"]) for pred in predictions]
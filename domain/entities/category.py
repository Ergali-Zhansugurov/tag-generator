from dataclasses import dataclass

@dataclass
class Category:
    name: str
    description: str

@dataclass
class Tag:
    name: str
    confidence: float  # Уверенность модели в теге
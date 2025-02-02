# domain/entities/book.py
from dataclasses import dataclass
from typing import List

@dataclass
class Review:
    text: str
    sentiment: str  # "POSITIVE", "NEGATIVE", "NEUTRAL"

@dataclass
class Book:
    title: str
    author: str
    description: str
    reviews: List[Review]
    summary: str = ""
    tags: List[str] = None
from dataclasses import dataclass
from typing import List

@dataclass
class Topic:
    def __init__(self, title, status="Not Initiated", comment=""):
        self.title = title
        self.status = status 
        self.comment = comment

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "comment": self.comment
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            status=data.get("status", "Not Initiated"),
            comment=data.get("comment", "")
        )

@dataclass
class Day:
    day_number: int
    title: str
    topics: List[Topic]

    def to_dict(self):
        return {
            "day": self.day_number,
            "title": self.title,
            "topics": [t.to_dict() for t in self.topics]
        }

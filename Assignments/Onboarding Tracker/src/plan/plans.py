from dataclasses import dataclass
from typing import List
from utils.utils import load_json_file
import json

@dataclass
class Topic:
    def __init__(self, title, status="Not Initiated", comment=""):
        self.title = title
        self.status = status  # Use string: "Done", "In Progress", "Not Initiated"
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

def load_learning_plan(plan_file_path: str) -> List[Day]:
    raw_data = load_json_file(plan_file_path)
    plan = []

    for day_entry in raw_data:
        day_number = day_entry['day']
        title = day_entry['title']
        topics = [Topic(title=topic_title) for topic_title in day_entry['topics']]
        plan.append(Day(day_number=day_number, title=title, topics=topics))

    return plan

def load_progress(filepath: str, plan: List[Day]):
    from pathlib import Path
    import json

    path = Path(filepath)
    if not path.exists() or path.stat().st_size == 0:
        # File doesn't exist or is empty; nothing to load
        print(f"No existing progress found. Starting fresh.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        try:
            progress_data = json.load(f)
        except json.JSONDecodeError:
            print(f"progress.json is empty or invalid JSON. Ignoring it.")
            return

    for saved_day in progress_data:
        for day in plan:
            if day.day_number == saved_day["day"]:
                for saved_topic in saved_day["topics"]:
                    for topic in day.topics:
                        if topic.title == saved_topic["title"]:
                            topic.status = saved_topic["status"]
                            topic.comment = saved_topic.get("comment", "")
                            break
                        
def save_json_file(filepath: str, data: list[dict]):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

from typing import List
import json

from utils.utils import load_json_file
from .models import Day, Topic

def load_learning_plan(plan_file_path: str):
    plan_data = load_json_file(plan_file_path)
    plan = []

    for day_entry in plan_data:
        day_number = day_entry.get("day", 0)
        title = day_entry.get("title", "")
        
        topics_data = day_entry.get("topics", []) 
        if not isinstance(topics_data, list):
            topics_data = []

        topics = [
            Topic.from_dict(t if isinstance(t, dict) else {"title": t})
            for t in topics_data
        ]

        plan.append(Day(day_number=day_number, title=title, topics=topics))

    return plan

def load_progress(filepath: str, plan: List[Day]):
    progress_data = load_json_file(filepath)

    for saved_day in progress_data:
        for day in plan:
            if day.day_number == saved_day["day"]:
                for saved_topic in saved_day["topics"]:
                    for topic in day.topics:
                        if topic.title == saved_topic["title"]:
                            topic.status = saved_topic["status"]
                            topic.comment = saved_topic.get("comment", "")
                            break
                        
    return plan
                        
def save_json_file(filepath: str, data: list[dict]):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

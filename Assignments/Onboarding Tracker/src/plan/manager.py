from .models import Day, Topic
from .plan_loader import load_learning_plan, load_progress, save_json_file

class PlanManager:
    def __init__(self, plan_file: str, progress_file: str):
        self.plan_file = plan_file
        self.progress_file = progress_file
        self.plan = load_learning_plan(plan_file)
        self.plan = load_progress(progress_file, self.plan)

    def get_plan(self):
        return self.plan

    def update_topic(self, day_number: int, topic_index: int, status: str, comment: str):
        day = next((d for d in self.plan if d.day_number == day_number), None)
        if not day:
            raise ValueError("Invalid day number")

        if topic_index < 0 or topic_index >= len(day.topics):
            raise IndexError("Invalid topic index")

        topic = day.topics[topic_index]
        topic.status = status
        topic.comment += '\n' + comment

    def save_progress(self):
        data = [day.to_dict() for day in self.plan]
        save_json_file(self.progress_file, data)

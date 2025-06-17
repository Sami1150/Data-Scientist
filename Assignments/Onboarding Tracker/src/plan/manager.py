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
        topic.comment += ('\n' if topic.comment else '') + comment

    def save_progress(self):
        data = [day.to_dict() for day in self.plan]
        save_json_file(self.progress_file, data)

    def save_plan(self):
        save_json_file(self.plan_file, [day.to_dict() for day in self.plan])

        
    def delete_plan(self, day_number: int):
        self.plan = [day for day in self.plan if day.day_number != day_number]
        self.save_plan()
        self.save_progress()
        
    def delete_topic(self, topic_number: int):
        topic_counter = 1
        for day in self.plan:
            for i, topic in enumerate(day.topics):
                if topic_counter == topic_number:
                    day.topics = [t for j, t in enumerate(day.topics) if j != i]
                    break
                topic_counter += 1
        self.save_plan()
        self.save_progress()


        
    def insert_day(self, day_number: int, title: str, topics: list[Topic]):
        if any(day.day_number == day_number for day in self.plan):
            raise ValueError(f"Day {day_number} already exists.")

        new_day = Day(day_number=day_number, title=title, topics=topics)
        self.plan.append(new_day)
        self.plan.sort(key=lambda d: d.day_number)
        self.save_plan()
        self.save_progress()



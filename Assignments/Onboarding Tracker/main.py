from plan.manager import PlanManager
from utils.display import display_plan_table
from plan.models import Topic

PLAN_FILE = "plan.json"
PROGRESS_FILE = "progress.json"

def main():
    manager = PlanManager(PLAN_FILE, PROGRESS_FILE)

    while True:
        print()
        display_plan_table(manager.get_plan(), None)

        print("\nOptions:")
        print("1. Update a topic")
        print("2. Delete a day and it's topics")
        print("3. Delete a topic")
        print("4. Insert a day and it's topics")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                day_number = int(input("Enter the day number: "))
                day = next((d for d in manager.get_plan() if d.day_number == day_number), None)
                if not day:
                    print("❌ Day not found.")
                    continue

                for i, topic in enumerate(day.topics, start=1):
                    print(f"{i}. {topic.title} (Status: {topic.status}, Comment: {topic.comment})")

                topic_index = int(input("Choose topic number: ")) - 1
                print("\n1. Done\n2. In Progress\n3. Not Initiated")
                status_choice = input("Choose status (1–3): ")
                status_map = {"1": "Done", "2": "In Progress", "3": "Not Initiated"}
                status = status_map.get(status_choice, "Not Initiated")
                comment = input("Comment (optional): ")

                manager.update_topic(day_number, topic_index, status, comment)
                manager.save_progress()
                print("✅ Topic updated.")

            except Exception as e:
                print(f"❌ {str(e)}")
        elif choice == "2":
            day_number = int(input("Enter the day number you want to delete: "))
            manager.delete_plan(day_number)
            manager.save_progress()
        elif choice == "3":
            plan = manager.get_plan()
            count = 1
            for day in plan:
                for topic in day.topics:
                    print(f"{count}. {topic.title} (Status: {topic.status}, Comment: '{topic.comment}')")
                    count += 1
            topic_number = int(input("Enter the topic you want to delete: "))
            print(topic_number)
            manager.delete_topic(topic_number)
            

        elif choice == "4":
            try:
                day_number = int(input("Enter new day number: "))
                existing_day = next((d for d in manager.get_plan() if d.day_number == day_number), None)

                if existing_day:
                    print(f"Day {day_number} already exists with title: '{existing_day.title}'")
                    new_title = input("Enter new title (or press Enter to keep current): ")
                    if new_title.strip():
                        existing_day.title = new_title  

                    num_topics = int(input("How many new topics to add? "))
                    for i in range(num_topics):
                        topic_title = input(f"  Topic {i+1} title: ")
                        existing_day.topics.append(Topic(title=topic_title)) 

                    print("✅ Day updated with new title/topics.")

                else:
                    title = input("Enter title for the new day: ")
                    num_topics = int(input("How many topics to add? "))

                    topics = []
                    for i in range(num_topics):
                        topic_title = input(f"  Topic {i+1} title: ")
                        topics.append(Topic(title=topic_title))

                    manager.insert_day(day_number, title, topics)
                    print("✅ New day and topics inserted.")

                manager.save_progress()

            except Exception as e:
                print(f"❌ {str(e)}")
        elif choice == "5":
            break
import numpy
if __name__ == "__main__":
    main()

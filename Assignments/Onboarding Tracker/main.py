from plan.manager import PlanManager
from utils.display import display_plan_table

PLAN_FILE = "plan.json"
PROGRESS_FILE = "progress.json"

def main():
    manager = PlanManager(PLAN_FILE, PROGRESS_FILE)

    while True:
        print()
        display_plan_table(manager.get_plan())

        print("\nOptions:")
        print("1. Update a topic")
        print("2. Exit")
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
            break

if __name__ == "__main__":
    main()

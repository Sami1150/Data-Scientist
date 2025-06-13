from plan import plans as plan_module
from utils import utils as utils_module

PROGRESS_FILE = "progress.json"

def update_topic_progress(plan):
    try:
        day_number = int(input("Enter the day number you want to update: "))
        day = next((d for d in plan if d.day_number == day_number), None)

        if not day:
            print("❌ Invalid day number.")
            return

        for i, topic in enumerate(day.topics, start=1):
            print(f"{i}. {topic.title} (Status: {topic.status}, Comment: '{topic.comment}')")

        topic_index = int(input("Enter the topic number to update: ")) - 1
        if topic_index < 0 or topic_index >= len(day.topics):
            print("❌ Invalid topic number.")
            return

        topic = day.topics[topic_index]

        print("\nSelect new status:")
        print("1. Done")
        print("2. In Progress")
        print("3. Not Initiated")
        status_choice = input("Choose status (1–3): ")

        status_map = {
            "1": "Done",
            "2": "In Progress",
            "3": "Not Initiated"
        }

        topic.status = status_map.get(status_choice, topic.status)
        topic.comment = input("Enter a comment (optional): ")

        print(f"✅ Updated: {topic.title} → {topic.status}")

        # Save progress after updating
        plan_module.save_json_file(PROGRESS_FILE, [day.to_dict() for day in plan])

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")


        
def main():
    plan = plan_module.load_learning_plan("plan.json")
    plan_module.load_progress("progress.json", plan)

    while True:
        print()
        utils_module.display_plan_table(plan)  # <— uses rich table instead of manual printing

        print("\nOptions:")
        print("1. Update a topic")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            update_topic_progress(plan)
        elif choice == "2":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

from rich.console import Console
from rich.table import Table
from rich.text import Text 
import json
from pathlib import Path


def load_json_file(filepath: str) -> list[dict]:
    """Loads and returns data from a JSON file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"{filepath} not found.")

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def display_plan_table(plan):
    console = Console()
    table = Table(title="Learning Plan Progress", show_lines=True)

    table.add_column("Day", style="bold cyan", no_wrap=True)
    table.add_column("Topic", style="bold magenta")
    table.add_column("Status", style="green")
    table.add_column("Comment", style="yellow")

    for day in plan:
        topics = day.topics
        topic_count = len(topics)
        
        # Combine Day number + title into a vertically aligned cell
        day_cell = Text(f"Day {day.day_number}\n{day.title}")
        first_topic = True

        for i, topic in enumerate(topics):
            table.add_row(
                day_cell if first_topic else "",  # Only show day info once
                topic.title,
                topic.status,
                topic.comment or ""
            )
            first_topic = False

    console.print(table)

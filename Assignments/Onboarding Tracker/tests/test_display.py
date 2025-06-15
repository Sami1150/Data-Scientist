import pytest
from rich.console import Console
from utils.display import display_plan_table
from plan.models import Day, Topic

def test_display_plan_table_renders_output():
    plan = [
        Day(1, "Python Basics", [
            Topic("Variables", "Done", "Understood well"),
            Topic("Loops", "In Progress", "")
        ])
    ]

    console = Console()
    with console.capture() as capture:
        display_plan_table(plan, console=console)
    
    output = capture.get()

    assert "Learning Plan Progress" in output
    assert "Day 1" in output
    assert "Python Basics" in output
    assert "Variables" in output
    assert "Done" in output
    assert "Understood well" in output
    assert "Loops" in output
    assert "In Progress" in output

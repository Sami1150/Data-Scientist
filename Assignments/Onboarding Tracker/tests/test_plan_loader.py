from plan.plan_loader import load_learning_plan, save_json_file, load_progress
from plan.models import Day, Topic
import tempfile
import os
import json
from unittest.mock import mock_open, patch


@patch("plan.plan_loader.load_json_file")
def test_load_learning_plan(mock_load_json_file):
    test_json = [
        {
            "day": 1,
            "title": "Intro to Python",
            "topics": ["Variables", "Data Types"]
        },
        {
            "day": 2,
            "title": "Control Flow",
            "topics": ["If Statements", "Loops"]
        }
    ]
    mock_load_json_file.return_value = test_json

    plan = load_learning_plan("dummy_path.json")

    assert isinstance(plan, list)
    assert len(plan) == 2
    assert isinstance(plan[0], Day)
    assert plan[0].day_number == 1
    assert plan[0].title == "Intro to Python"
    assert isinstance(plan[0].topics[0], Topic)
    assert plan[0].topics[0].title == "Variables"
    assert plan[0].topics[1].title == "Data Types"
    assert plan[1].day_number == 2
    assert plan[1].topics[1].title == "Loops"

@patch("plan.plan_loader.load_json_file")
def test_load_progress_updates_topic_status_and_comment(mock_load_json_file):
    plan = [
        Day(day_number=1, title="Intro", topics=[
            Topic(title="Variables"), 
            Topic(title="Data Types")
        ])
    ]

    test_progress = [
        {
            "day": 1,
            "topics": [
                {"title": "Variables", "status": "Done", "comment": "Easy"},
                {"title": "Data Types", "status": "In Progress", "comment": ""}
            ]
        }
    ]

    mock_load_json_file.return_value = test_progress

    load_progress("dummy_progress.json", plan)

    assert plan[0].topics[0].status == "Done"
    assert plan[0].topics[0].comment == "Easy"
    assert plan[0].topics[1].status == "In Progress"
    assert plan[0].topics[1].comment == ""
    
def test_save_json_file_writes_correct_data():
    test_data = [
        {"day": 1, "title": "Intro", "topics": [{"title": "Variables", "status": "Done", "comment": "OK"}]}
    ]

    m = mock_open()

    with patch("builtins.open", m):
        save_json_file("dummy.json", test_data)

    m.assert_called_once_with("dummy.json", 'w', encoding='utf-8')

    handle = m()
    written_data = ''.join(call.args[0] for call in handle.write.call_args_list)

    assert json.loads(written_data) == test_data

def test_save_json_file():
    data = [{"day": 1, "title": "Day 1", "topics": []}]
    
    with tempfile.NamedTemporaryFile(delete=False, mode='r+', encoding='utf-8') as tmp_file:
        filepath = tmp_file.name

    try:
        save_json_file(filepath, data)

        with open(filepath, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)

        assert saved_data == data
    finally:
        os.remove(filepath)
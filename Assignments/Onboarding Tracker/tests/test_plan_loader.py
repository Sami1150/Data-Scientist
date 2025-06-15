import pytest
from unittest.mock import patch
from plan.plan_loader import load_learning_plan
from plan.models import Day, Topic  # Adjust import path if needed
from plan.plan_loader import load_progress
import tempfile
import os

@patch("plan.plan_loader.load_json_file")
def test_load_learning_plan(mock_load_json_file):
    # Arrange: Setup fake JSON data
    fake_json = [
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
    mock_load_json_file.return_value = fake_json

    # Act
    plan = load_learning_plan("dummy_path.json")

    # Assert
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
    # Arrange: Create initial plan
    plan = [
        Day(day_number=1, title="Intro", topics=[
            Topic(title="Variables"), 
            Topic(title="Data Types")
        ])
    ]

    # Fake progress data to simulate progress.json
    fake_progress = [
        {
            "day": 1,
            "topics": [
                {"title": "Variables", "status": "Done", "comment": "Easy"},
                {"title": "Data Types", "status": "In Progress", "comment": ""}
            ]
        }
    ]

    mock_load_json_file.return_value = fake_progress

    # Act
    load_progress("dummy_progress.json", plan)

    # Assert
    assert plan[0].topics[0].status == "Done"
    assert plan[0].topics[0].comment == "Easy"
    assert plan[0].topics[1].status == "In Progress"
    assert plan[0].topics[1].comment == ""
    
import json
from unittest.mock import mock_open, patch
from plan.plan_loader import save_json_file  # Adjust path if needed

def test_save_json_file_writes_correct_data():
    # Sample data to save
    test_data = [
        {"day": 1, "title": "Intro", "topics": [{"title": "Variables", "status": "Done", "comment": "OK"}]}
    ]

    # Use mock_open to fake file writing
    m = mock_open()

    with patch("builtins.open", m):
        save_json_file("dummy.json", test_data)

    # Assert that file was opened correctly
    m.assert_called_once_with("dummy.json", 'w', encoding='utf-8')

    # Retrieve actual written data
    handle = m()
    written_data = ''.join(call.args[0] for call in handle.write.call_args_list)

    # Assert written content matches JSON-serialized data
    assert json.loads(written_data) == test_data

def test_save_json_file():
    # Sample data
    data = [{"day": 1, "title": "Day 1", "topics": []}]
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode='r+', encoding='utf-8') as tmp_file:
        filepath = tmp_file.name

    try:
        # Call the function to save data
        save_json_file(filepath, data)

        # Read the file to check the saved content
        with open(filepath, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)

        # Assert the content matches what we passed
        assert saved_data == data
    finally:
        # Cleanup: remove the temp file
        os.remove(filepath)
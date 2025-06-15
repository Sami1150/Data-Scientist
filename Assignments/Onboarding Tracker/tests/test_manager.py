import pytest
from unittest.mock import patch
from plan.manager import PlanManager  # ✅ update based on your project
from plan.models import Day, Topic  # Update paths based on your structure

# ✅ Patch where the function is used (plan.manager), not where it's defined (plan.plan_loader)
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_get_plan(mock_load_progress, mock_load_learning_plan):
    dummy_plan = ["Day 1", "Day 2"]
    mock_load_learning_plan.return_value = dummy_plan

    manager = PlanManager("dummy_plan.json", "dummy_progress.json")

    assert manager.get_plan() == dummy_plan
    
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_update_topic(mock_load_progress, mock_load_learning_plan):
    # Prepare dummy topic and day
    topic1 = Topic("Variables", "Not Initiated", "")
    topic2 = Topic("Loops", "Not Initiated", "")
    day = Day(1, "Python Basics", [topic1, topic2])

    # Mock plan loading
    mock_load_learning_plan.return_value = [day]

    # Create PlanManager
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")

    # Call method under test
    manager.update_topic(day_number=1, topic_index=0, status="Done", comment="Covered well")

    # Assertions
    updated_topic = manager.get_plan()[0].topics[0]
    assert updated_topic.status == "Done"
    assert updated_topic.comment == "Covered well"
    
@patch("plan.manager.save_json_file")
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_save_progress(mock_load_progress, mock_load_learning_plan, mock_save_json_file):
    # Prepare dummy data
    topic = Topic("Decorators", "Done", "Revised twice")
    day = Day(1, "Advanced Python", [topic])
    mock_load_learning_plan.return_value = [day]

    # Instantiate PlanManager
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")

    # Act
    manager.save_progress()

    # Assert save_json_file was called with expected data
    expected_data = [day.to_dict()]
    mock_save_json_file.assert_called_once_with("dummy_progress.json", expected_data)
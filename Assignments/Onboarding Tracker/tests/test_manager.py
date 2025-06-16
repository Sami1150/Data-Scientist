import pytest
from unittest.mock import patch
from plan.manager import PlanManager
from plan.models import Day, Topic 

@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_get_plan(mock_load_progress, mock_load_learning_plan):
    dummy_plan = ["Day 1", "Day 2"]
    mock_load_learning_plan.return_value = dummy_plan
    mock_load_progress.return_value = dummy_plan
    
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    print("sami", manager.get_plan())
    assert manager.get_plan() == dummy_plan
    
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_update_topic(mock_load_progress, mock_load_learning_plan):
    topic1 = Topic("Variables", "Not Initiated", "")
    topic2 = Topic("Loops", "Not Initiated", "")
    day = Day(1, "Python Basics", [topic1, topic2])

    mock_load_learning_plan.return_value = [day]
    mock_load_progress.return_value = [day]
    
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")

    manager.update_topic(day_number=1, topic_index=0, status="Done", comment="Covered well")

    updated_topic = manager.get_plan()[0].topics[0]
    assert updated_topic.status == "Done"
    assert updated_topic.comment == "Covered well"
    
@patch("plan.manager.save_json_file")
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_save_progress(mock_load_progress, mock_load_learning_plan, mock_save_json_file):
    topic = Topic("Decorators", "Done", "Revised twice")
    day = Day(1, "Advanced Python", [topic])
    mock_load_learning_plan.return_value = [day]
    mock_load_progress.return_value = [day]
    
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")

    manager.save_progress()

    expected_data = [day.to_dict()]
    mock_save_json_file.assert_called_once_with("dummy_progress.json", expected_data)
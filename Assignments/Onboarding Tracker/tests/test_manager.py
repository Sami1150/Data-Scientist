import pytest
from unittest.mock import patch
from plan.manager import PlanManager
from plan.models import Day, Topic


@pytest.fixture
def mock_plan():
    topic1 = Topic("T1", "Not Started", "")
    topic2 = Topic("T2", "Not Started", "")
    day1 = Day(day_number=1, title="Day 1", topics=[topic1])
    day2 = Day(day_number=2, title="Day 2", topics=[topic2])
    return [day1, day2]


@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_get_plan(mock_load_progress, mock_load_learning_plan, mock_plan):
    mock_load_learning_plan.return_value = mock_plan
    mock_load_progress.return_value = mock_plan
    
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    assert manager.get_plan() == mock_plan


@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_update_topic(mock_load_progress, mock_load_learning_plan, mock_plan):
    mock_load_learning_plan.return_value = mock_plan
    mock_load_progress.return_value = mock_plan
    
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    manager.update_topic(day_number=1, topic_index=0, status="Done", comment="Covered well")

    updated_topic = manager.get_plan()[0].topics[0]
    assert updated_topic.status == "Done"
    assert updated_topic.comment == "Covered well"


@patch("plan.manager.save_json_file")
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_save_progress(mock_load_progress, mock_load_learning_plan, mock_save_json_file, mock_plan):
    mock_load_learning_plan.return_value = mock_plan
    mock_load_progress.return_value = mock_plan
    
    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    manager.save_progress()

    expected_data = [day.to_dict() for day in mock_plan]
    mock_save_json_file.assert_called_once_with("dummy_progress.json", expected_data)


@patch("plan.manager.save_json_file")
@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_save_plan(mock_load_progress, mock_load_learning_plan, mock_save_json_file, mock_plan):
    mock_load_learning_plan.return_value = mock_plan
    mock_load_progress.return_value = mock_plan

    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    manager.save_plan()

    expected_data = [day.to_dict() for day in mock_plan]
    mock_save_json_file.assert_called_once_with("dummy_plan.json", expected_data)


@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_delete_plan(mock_load_progress, mock_load_learning_plan, mock_plan):
    mock_load_learning_plan.return_value = mock_plan
    mock_load_progress.return_value = mock_plan

    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    manager.delete_plan(1)
    assert len(manager.get_plan()) == 1


@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_delete_topic(mock_load_progress, mock_load_learning_plan, mock_plan):
    mock_load_learning_plan.return_value = mock_plan
    mock_load_progress.return_value = mock_plan

    manager = PlanManager("dummy_plan.json", "dummy_progress.json")
    manager.delete_topic(2) 

    updated_plan = manager.get_plan()
    assert len(updated_plan[0].topics) == 1
    assert updated_plan[0].topics[0].title == "T1"
    assert len(updated_plan[1].topics) == 0


@patch("plan.manager.load_learning_plan")
@patch("plan.manager.load_progress")
def test_insert_day_success(mock_load_progress, mock_load_learning_plan, mock_plan):
    mock_load_learning_plan.return_value = mock_plan[:1]  
    mock_load_progress.return_value = mock_plan[:1]

    manager = PlanManager("dummy_plan.json", "dummy_progress.json")

    new_topics = [Topic("T2"), Topic("T3")]
    manager.insert_day(day_number=2, title="Day 2", topics=new_topics)

    plan = manager.get_plan()
    assert len(plan) == 2
    assert plan[0].day_number == 1
    assert plan[1].day_number == 2
    assert plan[1].title == "Day 2"
    assert len(plan[1].topics) == 2
    assert plan[1].topics[0].title == "T2"
    
    # assert_called_once_with
    # assert_called_twice_with


import pytest
import json
import tempfile
import os
from utils.utils import load_json_file


def test_load_json_file_success():
    test_data = [{"name": "Alice"}, {"name": "Bob"}]

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as tmp:
        json.dump(test_data, tmp)
        tmp_path = tmp.name

    try:
        result = load_json_file(tmp_path)
        assert result == test_data
    finally:
        os.remove(tmp_path)


def test_load_json_file_not_found():
    result = load_json_file("nonexistent_file.json")
    assert result == []


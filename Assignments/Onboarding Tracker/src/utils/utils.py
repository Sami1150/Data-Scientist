import json
from pathlib import Path


def load_json_file(filepath: str) -> list[dict]:
    """Loads and returns data from a JSON file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"{filepath} not found.")

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

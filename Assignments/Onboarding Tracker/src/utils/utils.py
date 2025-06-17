import json

def load_json_file(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
        

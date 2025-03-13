import json
from src import data

def load_level():
    with open(f"levels/{data.current_level}.json", "r") as f:
        return json.load(f)
    
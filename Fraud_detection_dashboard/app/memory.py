import json
import os

def save_feedback(feedback, path="feedback.json"):
    with open(path, "w") as f:
        json.dump(feedback, f, indent=2)

def load_feedback(path="feedback.json"):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {} 
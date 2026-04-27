import json
import os

FILE_NAME = "scores.json"

def load_scores():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_score(name, score, distance):
    scores = load_scores()

    scores.append({
        "name": name,
        "score": score,
        "distance": distance
    })

    scores = sorted(scores, key=lambda x: x["score"], reverse=True)
    scores = scores[:10]

    with open(FILE_NAME, "w") as file:
        json.dump(scores, file, indent=4)

def get_top_scores():
    return load_scores()
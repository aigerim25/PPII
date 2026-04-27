import json


def load_config():
    with open("settings.json", "r") as file:
        return json.load(file)


def save_config(data):
    with open("settings.json", "w") as file:
        json.dump(data, file, indent=4)
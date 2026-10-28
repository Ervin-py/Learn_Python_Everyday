import json

def load_drawings():
    try:
        with open("drawings.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("drawings.json not found")
        return []
    except json.JSONDecodeError:
        print("JSON file is corrupted")
        return []

def save_drawings(drawing):
    try:
        with open("drawings.json", "w") as file:
            json.dump(drawing, file, indent=4)

    except OSError:
        print("Error saving file")
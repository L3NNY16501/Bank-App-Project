import json

def load_users() -> dict:
    try:
        with open("user_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: File not found")
    
def save_users(data) -> None:#
    try:
        with open("user_data.json", "w") as f:
            json.dump(data, f, indent=4)
    except FileNotFoundError:
        print("Error: File not found")
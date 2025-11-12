import json

def load_users() -> dict:
    with open("user_data.json", "r") as f:
        return json.load(f)
    
def save_users(data) -> None:
    with open("user_data.json", "w") as f:
        json.dump(data, f, indent=4)
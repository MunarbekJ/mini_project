import json

def get_db() -> dict:
    with open("db.json") as file:
        return json.load(file)
    
def get_pages() -> list:
    db = get_db()
    return list(db.keys())
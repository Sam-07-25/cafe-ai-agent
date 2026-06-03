import json
import os

RESERVATIONS_FILE = "reservations.json" # all reservations are appended to this file

def load_reservations():
    if os.path.exists(RESERVATIONS_FILE):
        with open(RESERVATIONS_FILE, "r") as f:
            return json.load(f)
    return []

def save_reservations(reservations):
    with open(RESERVATIONS_FILE, "w") as f:
        json.dump(reservations, f, indent=2)

def delete_reservation(name: str, date: str, time: str):
    reservations = load_reservations()
    
    original_count = len(reservations)
    
    reservations = [
        r for r in reservations
        if not (r["name"].lower() == name.lower() and 
                r["date"].lower() == date.lower() and 
                r["time"].lower() == time.lower())
    ]
    
    if len(reservations) == original_count:
        return False  # nothing was deleted
    
    save_reservations(reservations)
    return True  # successfully deleted
import json
import os

RESERVATIONS_FILE = "reservations.json"

def load_reservations():
    if os.path.exists(RESERVATIONS_FILE):
        with open(RESERVATIONS_FILE, "r") as f:
            return json.load(f)
    return []

def save_reservations(reservations):
    with open(RESERVATIONS_FILE, "w") as f:
        json.dump(reservations, f, indent=2)
        
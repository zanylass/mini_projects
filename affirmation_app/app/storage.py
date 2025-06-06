import os
import datetime
import random

AFFIRMATION_FILE = "affirmations.txt"
MANIFESTATION_FILE = "manifestations.txt"

def save_entry(filename, text):
    today = datetime.date.today().isoformat()
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{today}: {text}\n")

def load_entries(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_random_entry():
    all_entries = load_entries(AFFIRMATION_FILE) + load_entries(MANIFESTATION_FILE)
    if not all_entries:
        return None
    entry = random.choice(all_entries)
    return entry.split(":", 1)[1].strip() if ":" in entry else entry

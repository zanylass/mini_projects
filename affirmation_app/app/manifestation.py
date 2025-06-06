import datetime
from app.storage import save_entry, load_entries

MANIFESTATION_FILE = "manifestations.txt"

def add_manifestation():
    text = input("Enter your manifestation mantra: ").strip()
    if text:
        save_entry(MANIFESTATION_FILE, text)
        print("Manifestation saved!")
    else:
        print("Empty manifestation not saved.")

def view_today_manifestations():
    today = datetime.date.today().isoformat()
    entries = load_entries(MANIFESTATION_FILE)
    today_entries = [e for e in entries if e.startswith(today)]
    if not today_entries:
        print("No manifestations added for today.")
    else:
        print("🌌 Today's Manifestations:")
        for e in today_entries:
            print("-", e.split(":", 1)[1].strip())

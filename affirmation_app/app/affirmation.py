import datetime
from app.storage import save_entry, load_entries

AFFIRMATION_FILE = "affirmations.txt"

def add_affirmation():
    text = input("Enter your affirmation: ").strip()
    if text:
        save_entry(AFFIRMATION_FILE, text)
        print("Affirmation saved!")
    else:
        print("Empty affirmation not saved.")

def view_today_affirmations():
    today = datetime.date.today().isoformat()
    entries = load_entries(AFFIRMATION_FILE)
    today_entries = [e for e in entries if e.startswith(today)]
    if not today_entries:
        print("No affirmations added for today.")
    else:
        print("🌠Today's Affirmations:")
        for e in today_entries:
            print("-", e.split(":", 1)[1].strip())

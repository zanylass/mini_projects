from app.affirmation import add_affirmation, view_today_affirmations
from app.manifestation import add_manifestation, view_today_manifestations
from app.storage import get_random_entry

def main_menu():
    while True:
        print("\n=== Manifestation & Affirmation App ===")
        print("1. Add Affirmation")
        print("2. Add Manifestation Mantra")
        print("3. View Today's Affirmations")
        print("4. View Today's Manifestations")
        print("5. Get Random Affirmation or Manifestation")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            add_affirmation()
        elif choice == '2':
            add_manifestation()
        elif choice == '3':
            view_today_affirmations()
        elif choice == '4':
            view_today_manifestations()
        elif choice == '5':
            random_item = get_random_entry()
            if random_item:
                print(f"\n✨ Here's something for you:\n→ {random_item}")
            else:
                print("\nNo affirmations or manifestations found yet.")
        elif choice == '6':
            print("\nGoodbye! Stay positive 🌟")
            break
        else:
            print("\nInvalid choice. Please try again.")

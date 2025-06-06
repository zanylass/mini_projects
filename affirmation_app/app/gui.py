import tkinter as tk
from tkinter import messagebox, simpledialog
from app.affirmation import add_affirmation, view_today_affirmations
from app.manifestation import add_manifestation, view_today_manifestations
from app.storage import get_random_entry

def run_gui():
    root = tk.Tk()
    root.title("Manifestation & Affirmation App")
    root.geometry("400x400")

    def handle_add_affirmation():
        text = simpledialog.askstring("Add Affirmation", "Enter your affirmation:")
        if text:
            add_affirmation_manual(text)
            messagebox.showinfo("Success", "Affirmation saved!")

    def handle_add_manifestation():
        text = simpledialog.askstring("Add Manifestation", "Enter your manifestation mantra:")
        if text:
            add_manifestation_manual(text)
            messagebox.showinfo("Success", "Manifestation saved!")

    def show_today_affirmations():
        affirmations = view_today_affirmations(return_output=True)
        messagebox.showinfo("Today's Affirmations", affirmations)

    def show_today_manifestations():
        manifestations = view_today_manifestations(return_output=True)
        messagebox.showinfo("Today's Manifestations", manifestations)

    def show_random_entry():
        entry = get_random_entry()
        if entry:
            messagebox.showinfo("✨ Random Inspiration", entry)
        else:
            messagebox.showinfo("Info", "No entries yet.")

    # Buttons
    tk.Button(root, text="Add Affirmation", command=handle_add_affirmation, width=30).pack(pady=5)
    tk.Button(root, text="Add Manifestation", command=handle_add_manifestation, width=30).pack(pady=5)
    tk.Button(root, text="View Today's Affirmations", command=show_today_affirmations, width=30).pack(pady=5)
    tk.Button(root, text="View Today's Manifestations", command=show_today_manifestations, width=30).pack(pady=5)
    tk.Button(root, text="Get Random Entry", command=show_random_entry, width=30).pack(pady=5)

    tk.Label(root, text="Stay Positive ✨", font=("Arial", 10)).pack(pady=20)

    root.mainloop()


# These are GUI-friendly wrapper versions of the original functions
def add_affirmation_manual(text):
    from app.storage import save_entry
    save_entry("affirmations.txt", text)

def add_manifestation_manual(text):
    from app.storage import save_entry
    save_entry("manifestations.txt", text)

# Modified versions for display purposes
def view_today_affirmations(return_output=False):
    from datetime import date
    from app.storage import load_entries
    today = date.today().isoformat()
    entries = load_entries("affirmations.txt")
    today_entries = [e for e in entries if e.startswith(today)]
    if not today_entries:
        return "No affirmations added today."
    output = "\n".join("- " + e.split(":", 1)[1].strip() for e in today_entries)
    return output

def view_today_manifestations(return_output=False):
    from datetime import date
    from app.storage import load_entries
    today = date.today().isoformat()
    entries = load_entries("manifestations.txt")
    today_entries = [e for e in entries if e.startswith(today)]
    if not today_entries:
        return "No manifestations added today."
    output = "\n".join("- " + e.split(":", 1)[1].strip() for e in today_entries)
    return output

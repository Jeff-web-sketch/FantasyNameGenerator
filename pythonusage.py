import requests
import random
import json
from datetime import datetime

# --- CONFIGURATION ---
# Replace with your GitHub details
GITHUB_USER = "jeff-web-sketch"
GITHUB_REPO = "FantasyNameGenerator"
BRANCH = "main"
DATA_FILE = "data.json"

# Use raw.githubusercontent.com for Python scripts
RAW_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/{DATA_FILE}"

def fetch_data():
    """Fetches the JSON data from GitHub."""
    try:
        response = requests.get(RAW_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def generate_names(data, category, count=10):
    """Generates names from the fetched data."""
    if category not in data:
        print(f"Category '{category}' not found in data.")
        return []

    starts = data[category]['starts']
    ends = data[category]['ends']
    names = []
    
    for _ in range(count):
        s = random.choice(starts)
        e = random.choice(ends)
        # Force compound format (StartEnd) like the website
        name = f"{s}{e}"
        names.append(name)
    
    return names

def save_to_file(saved_collection, filename="saved_names.txt"):
    """Saves the collection of names to a text file with sections."""
    if not saved_collection:
        print("No names to save.")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write("FANTASY NAME GENERATOR - SAVED COLLECTION\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("==========================================\n\n")

        for category, names in saved_collection.items():
            title = category.capitalize()
            f.write(f"--- {title} Names ---\n")
            for name in names:
                f.write(f"{name}\n")
            f.write("\n")
    
    print(f"Successfully saved names to '{filename}'")

def main():
    print(f"Fetching data from GitHub...")
    data = fetch_data()
    
    if not data:
        print("Failed to load data. Check your internet connection or GitHub URL.")
        return

    print("Data loaded successfully!")
    categories = list(data.keys())
    print(f"Available generators: {', '.join([c.capitalize() for c in categories])}\n")

    saved_collection = {} # Dictionary to store lists of names: {'dragon': ['FireScale', ...]}

    while True:
        choice = input(f"Select category ({', '.join(categories)}) or 'quit': ").lower()
        if choice == 'quit':
            break
        
        if choice not in data:
            print("Invalid category. Try again.\n")
            continue

        try:
            count = int(input("How many names to generate? (default 10): ") or "10")
        except ValueError:
            count = 10

        names = generate_names(data, choice, count)
        
        print(f"\n✨ {choice.capitalize()} Names:")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
        
        # Ask to save
        save_choice = input("Save these names? (y/n): ").lower()
        if save_choice == 'y':
            if choice not in saved_collection:
                saved_collection[choice] = []
            saved_collection[choice].extend(names)
            print(f"Added {len(names)} names to your saved collection.\n")
        else:
            print()

    # Final Export
    if saved_collection:
        export = input("Download saved collection to .txt file? (y/n): ").lower()
        if export == 'y':
            save_to_file(saved_collection)
    else:
        print("No names were saved during this session.")

if __name__ == "__main__":
    main()   
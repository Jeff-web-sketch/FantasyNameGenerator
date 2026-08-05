import requests
import random
import json

DEFAULT_DATA_URL = "https://raw.githubusercontent.com/jeff-web-sketch/FantasyNameGenerator/main/data.json"

class NameGenerator:
    def __init__(self, data_url=DEFAULT_DATA_URL):
        self.data_url = data_url
        self.data = None
        self._fetch_data()

    def _fetch_data(self):
        """Fetches data from GitHub on initialization."""
        try:
            response = requests.get(self.data_url)
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch name data: {e}")

    def get_categories(self):
        """Returns a list of available categories."""
        return list(self.data.keys()) if self.data else []

    def generate(self, category, count=10, format_type="compound"):
        """
        Generates names for a specific category.
        
        Args:
            category (str): The type of name (e.g., 'dragon', 'elf').
            count (int): Number of names to generate.
            format_type (str): 'compound' (StartEnd) or 'of' (Start of End).
        
        Returns:
            list: A list of generated names.
        """
        if not self.data or category not in self.data:
            raise ValueError(f"Category '{category}' not found. Available: {self.get_categories()}")

        starts = self.data[category]['starts']
        ends = self.data[category]['ends']
        names = []

        for _ in range(count):
            s = random.choice(starts)
            e = random.choice(ends)
            
            if format_type == "of":
                name = f"{s} of {e}"
            else:
                name = f"{s}{e}"
            names.append(name)
        
        return names

    def export_to_file(self, saved_collection, filename="saved_names.txt"):
        """Exports a dictionary of saved names to a text file."""
        from datetime import datetime
        
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
        return filename   
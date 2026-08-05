from fantasy_name_generator import NameGenerator

def main():
    print("🐍 Fantasy Name Generator CLI")
    try:
        generator = NameGenerator()
    except RuntimeError as e:
        print(f"Error: {e}")
        return

    categories = generator.get_categories()
    print(f"Available: {', '.join(categories)}\n")

    saved_collection = {}

    while True:
        choice = input(f"Select category ({', '.join(categories)}) or 'quit': ").lower()
        if choice == 'quit':
            break
        
        if choice not in categories:
            print("Invalid category.\n")
            continue

        try:
            count = int(input("How many names? (default 10): ") or "10")
        except ValueError:
            count = 10

        names = generator.generate(choice, count)
        
        print(f"\n✨ {choice.capitalize()} Names:")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
        
        if input("Save these? (y/n): ").lower() == 'y':
            if choice not in saved_collection:
                saved_collection[choice] = []
            saved_collection[choice].extend(names)
            print("Saved.\n")

    if saved_collection:
        if input("Download collection? (y/n): ").lower() == 'y':
            filename = generator.export_to_file(saved_collection)
            print(f"Saved to {filename}")

if __name__ == "__main__":
    main()   
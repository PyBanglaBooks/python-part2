import json
from pathlib import Path

FILE = Path("contacts.json")


def load_contacts():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return []


def save_contacts(contacts):
    text = json.dumps(contacts, indent=4, ensure_ascii=False)
    FILE.write_text(text, encoding="utf-8")


def show_contacts(contacts):
    for contact in contacts:
        print(f"{contact['name']}: {contact['phone']}")


def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"{name} added.")


def search_contacts(contacts):
    word = input("Search: ").lower()
    found = [c for c in contacts if word in c["name"].lower()]
    if found:
        show_contacts(found)
    else:
        print("Nothing found.")


def main():
    contacts = load_contacts()
    while True:
        print()
        print("1. Add  2. Show all  3. Search  0. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Please enter 0, 1, 2 or 3.")


if __name__ == "__main__":
    main()

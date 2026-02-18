from firestore_db import get_db
from models import (
    create_user, get_all_users, get_user_by_id, delete_user,
    create_entry, get_entries, update_entry, delete_entry
)


def prompt_int(message, allow_blank=False):
    """Prompt for an int; optionally allow blank input."""
    while True:
        value = input(message).strip()
        if allow_blank and value == "":
            return None
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def choose_user(db):
    """Show users and allow picking by userId."""
    users = get_all_users(db)
    if not users:
        print("No users found. Create a user first.")
        return ""

    print("\n--- USERS ---")
    for u in users:
        print(f"ID: {u['id']} | {u.get('name')} | {u.get('email')}")

    user_id = input("Enter a User ID: ").strip()
    if not get_user_by_id(db, user_id):
        print("User not found.")
        return ""
    return user_id


def menu():
    print("\n=== Cloud Fitness Tracker (Firestore) ===")
    print("1) Create User (INSERT)")
    print("2) Create Entry (INSERT)")
    print("3) View Entries (RETRIEVE / QUERY)")
    print("4) Update Entry (MODIFY)")
    print("5) Delete Entry (DELETE)")
    print("6) Delete User (DELETE)")
    print("0) Exit")


def main():
    db = get_db("serviceAccountKey.json")

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        # 1) Create User
        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            user_id = create_user(db, name, email)
            print(f"✅ User created! userId = {user_id}")

        # 2) Create Entry
        elif choice == "2":
            user_id = choose_user(db)
            if not user_id:
                continue

            entry_type = input("Entry type (meal/workout): ")
            title = input("Title: ")
            calories = prompt_int("Calories (optional, press Enter to skip): ", allow_blank=True)
            duration = prompt_int("Duration minutes (optional, press Enter to skip): ", allow_blank=True)

            entry_id = create_entry(db, user_id, entry_type, title, calories, duration)
            print(f"✅ Entry created! entryId = {entry_id}")

        # 3) View Entries
        elif choice == "3":
            only_one = input("View entries for a specific user? (y/n): ").strip().lower()
            if only_one == "y":
                user_id = choose_user(db)
                if not user_id:
                    continue
                entries = get_entries(db, user_id=user_id)
            else:
                entries = get_entries(db)

            if not entries:
                print("No entries found.")
                continue

            print("\n--- ENTRIES ---")
            for e in entries:
                print("-" * 40)
                print(f"Entry ID: {e['id']}")
                print(f"userId: {e.get('userId')}")
                print(f"type: {e.get('type')}")
                print(f"title: {e.get('title')}")
                print(f"calories: {e.get('calories', 'N/A')}")
                print(f"duration: {e.get('duration', 'N/A')}")
                print(f"createdAt: {e.get('createdAt')}")

        # 4) Update Entry
        elif choice == "4":
            entry_id = input("Enter Entry ID to update: ").strip()
            print("Leave blank to skip a field.")

            new_title = input("New title: ").strip()
            new_type = input("New type (meal/workout): ").strip()
            new_calories = prompt_int("New calories (blank to skip): ", allow_blank=True)
            new_duration = prompt_int("New duration (blank to skip): ", allow_blank=True)

            updates = {}
            if new_title:
                updates["title"] = new_title
            if new_type:
                updates["type"] = new_type.lower()
            if new_calories is not None:
                updates["calories"] = new_calories
            if new_duration is not None:
                updates["duration"] = new_duration

            if not updates:
                print("No updates provided.")
                continue

            update_entry(db, entry_id, updates)
            print("✅ Entry updated!")

        # 5) Delete Entry
        elif choice == "5":
            entry_id = input("Enter Entry ID to delete: ").strip()
            delete_entry(db, entry_id)
            print("✅ Entry deleted!")

        # 6) Delete User
        elif choice == "6":
            user_id = choose_user(db)
            if not user_id:
                continue
            confirm = input("Delete this user? (y/n): ").strip().lower()
            if confirm == "y":
                delete_user(db, user_id)
                print("✅ User deleted!")
            else:
                print("Cancelled.")

        # Exit
        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

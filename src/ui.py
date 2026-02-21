def pause():
    input("\nPress Enter to continue...")


def print_divider():
    print("-" * 40)


def print_request(row):
    if row is None:
        print("Request not found.")
        return
    req_id, title, description, status, created_at, updated_at = row
    print_divider()
    print(f"ID: {req_id}")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Status: {status.title()}")
    print(f"Created at: {created_at}")
    print(f"Updated at: {updated_at}")
    print_divider()


def print_menu():
    print("\n=== Change Request Management System ===")
    print("1. Add Change Request")
    print("2. View All Requests")
    print("3. View Request by ID")
    print("4. Update Request Status")
    print("5. Delete Request")
    print("6. Exit")


def prompt_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")


def prompt_non_empty(field_name: str) -> str | None:
    while True:
        value = input(f"Enter {field_name} (or 'q' to cancel): ").strip()

        if value.lower() == "q":
            return None

        if not value:
            print(f"{field_name.capitalize()} cannot be empty.")
            continue

        return value

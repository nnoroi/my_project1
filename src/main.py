from database import create_table
from database import get_db_connection
from services import (
    add_change_request,
    get_all_change_requests,
    get_change_request_by_id,
    update_change_request_status,
    delete_change_request_by_id,
)


def print_menu():
    print("\n=== Change Request Management System ===")
    print("1. Add Change Request")
    print("2. View All Requests")
    print("3. View Request by ID")
    print("4. Update Request Status")
    print("5. Delete Request")
    print("6. Exit")


def promt_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")


def handle_create():
    title = input("Enter title: ").strip()
    description = input("Enter description: ").strip()

    if not title or not description:
        print("Title and description cannot be empty.")
        return

    new_id = add_change_request(title=title, description=description)
    print(f"Created change request with ID: {new_id}")


def handle_view_all():
    rows = get_all_change_requests()
    if not rows:
        print("No change requests found.")
        return

    print("\nAll changes requests:")
    for row in rows:
        print("\n------------------------------")
        print(f"ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Description: {row[2]}")
        print(f"Status: {row[3].title()}")
        print(f"Created at: {row[4]}")
        print(f"Updated at: {row[5]}")


def handle_view_by_id():
    request_id = promt_int("Enter ID: ")
    row = get_change_request_by_id(request_id)

    if row is None:
        print("Request not found.")
        return

    print("\n--- Change request ---")
    print("------------------------------")
    if len(row) == 7:
        print(f"ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Description: {row[2]}")
        print(f"Status: {row[3].title()}")
        print(f"Created at: {row[4]}")
        print(f"Updated at: {row[5]}")
    else:
        print(row)


def handle_update_status():
    request_id = promt_int("Enter ID:")
    new_status = input(
        "New status (pending/approved/rejected): ").strip().lower()

    try:
        updated = update_change_request_status(request_id, new_status)

    except ValueError:
        print("Invalid status. Use pending / approved / rejected.")
        return

    if updated == 0:
        print("Request not found.")
    else:
        print("Status updated successfully.")


def handle_delete():
    request_id = promt_int("Enter ID: ")
    confirm = input(
        "Are you sure you want to delete this request? (y/n): ").strip().lower()

    if confirm != "y":
        print(" Deletion cancelled.")
        return

    deleted = delete_change_request_by_id(request_id)
    if deleted == 0:
        print("Request not found.")
    else:
        print("Request deleted successfully.")


def main():

    create_table()

    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            handle_create()
        elif choice == "2":
            handle_view_all()
        elif choice == "3":
            handle_view_by_id()
        elif choice == "4":
            handle_update_status()
        elif choice == "5":
            handle_delete()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick from 1-6.")


if __name__ == "__main__":
    main()

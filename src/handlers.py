from ui import print_menu, print_request, prompt_int, prompt_non_empty, pause
from services import (
    add_change_request,
    get_all_change_requests,
    get_change_request_by_id,
    update_change_request_status,
    delete_change_request_by_id
)


def handle_create():
    title = prompt_non_empty("title")
    if title is None:
        print("Creation cancelled.")
        pause()
        return

    description = prompt_non_empty("description")
    if description is None:
        print("Creation cancelled.")
        pause()
        return

    new_id = add_change_request(title=title, description=description)
    print(f"Created change request with ID: {new_id}")
    pause()


def handle_view_all():
    rows = get_all_change_requests()
    if not rows:
        print("No change requests found.")
        return

    print("\nAll changes requests:")
    for row in rows:
        print_request(row)

    pause()


def handle_view_by_id():
    request_id = prompt_int("Enter ID: ")
    row = get_change_request_by_id(request_id)
    print_request(row)
    pause()


def handle_update_status():
    request_id = prompt_int("Enter ID:")

    while True:
        new_status = input(
            "New status (pending/approved/rejected) or 'q' to cancel: ").strip().lower()
        if new_status == "q":
            print("Update cancelled.")
            pause()
            return
        try:
            updated = update_change_request_status(request_id, new_status)

            if updated == 0:
                print("Request not found.")
                pause()
                return
            print("Status updated successfully.")
            print("Updated request:")
            print_request(get_change_request_by_id(request_id))
            pause()
            break

        except ValueError:
            print("Invalid status. Use pending / approved / rejected.")


def handle_delete():
    request_id = prompt_int("Enter ID to delete: ")
    row = get_change_request_by_id(request_id)
    if row is None:
        print("Request not found.")
        pause()
        return

    print("You are about to delete:")
    print_request(row)
    confirm = input("Type 'DELETE' to confirm: ").strip()
    if confirm != "DELETE":
        print("Deletion cancelled.")
        pause()
        return

    deleted = delete_change_request_by_id(request_id)
    print("Deleted successfully." if deleted else "Request not found.")
    pause()


def run_cli():
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

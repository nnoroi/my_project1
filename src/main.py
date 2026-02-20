from database import create_table
from services import get_all_change_requests, get_change_request_by_id, update_change_request_status


def main():
    create_table()

    print("\nAll changes requests:")
    rows = get_all_change_requests()

    for row in rows:
        print("\n------------------------------")
        print(f"ID: {row[0]}")
        print(f"Title: {row[1]}")
        print(f"Description: {row[2]}")
        print(f"Status: {row[3].title()}")
        print(f"Created at: {row[4]}")

    print("\nSingle request (ID = 1):")
    row = get_change_request_by_id(1)

    if row is None:
        print("Not Found")
    else:
        print(row)

    print("\nUpdating status of ID 1 to Approved...")
    updated = update_change_request_status(1, "Approved")

    if updated == 0:
        print("No record found.")

    else:
        print("\nChange Request Updated Successfully.")

        updated_request = get_change_request_by_id(1)

        print("------------------------------")
        print(f"ID: {updated_request[0]}")
        print(f"Title: {updated_request[1]}")
        print(f"Status: {updated_request[3].title()}")
        print(f"Updated at: {updated_request[5]}")


if __name__ == "__main__":
    main()

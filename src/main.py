from database import create_table
from services import add_change_request


def main():
    create_table()
    new_id = add_change_request(
        title="Update University Portal",
        description="Improve login flow before release"
    )

    print(f"Added request with ID: {new_id}")


if __name__ == "__main__":
    main()

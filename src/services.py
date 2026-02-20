from datetime import datetime
from database import get_db_connection

ALLOWED_STATUSES = ["pending", "approved", "rejected"]


def add_change_request(title: str, description: str) -> int:
    """Creates a new change request with status 'pending'.
       Returns the new record ID.
    """

    now = datetime.now().isoformat(timespec="seconds")
    conn = get_db_connection()

    try:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO change_requests (title, description, status, created_at, updated_at)
                       VALUES (?, ?, ?, ?, ?)
                       """, (title, description, "pending", now, now))

        conn.commit()

        return cursor.lastrowid

    finally:
        conn.close()

from datetime import datetime
from database import get_db_connection

ALLOWED_STATUSES = {"pending", "approved", "rejected"}


def add_change_request(title: str, description: str) -> int:
    conn = get_db_connection()
    now = datetime.now().isoformat(timespec="seconds")
    try:
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO change_requests (title, description, status, created_at, updated_at)
                       VALUES (?, ?, ?, ?, ?)
                       """, (title, description, "pending", now, now)
                       )
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def update_change_request_status(request_id: int, new_status: str) -> int:
    new_status = new_status.lower().strip()

    if new_status not in ALLOWED_STATUSES:
        raise ValueError("Invalid status")

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE change_requests
            SET status = ?, updated_at = ?
            WHERE id = ?
        """, (new_status, datetime.now().isoformat(timespec="seconds"), request_id))

        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()


def get_all_change_requests():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, title, description, status, created_at, updated_at
            FROM change_requests
            ORDER BY id DESC
        """)
        return cursor.fetchall()
    finally:
        conn.close()


def get_change_request_by_id(request_id: int):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, title, description, status, created_at, updated_at
            FROM change_requests
            WHERE id = ?
        """, (request_id,))
        return cursor.fetchone()
    finally:
        conn.close()


def delete_change_request_by_id(request_id: int) -> int:
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
                       DELETE FROM change_requests
                       WHERE id = ?
                       """, (request_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        conn.close()

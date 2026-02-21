My project: Change Request Tracker (CLI)

# Change Request Tracker (CLI)

A simple command-line Change Management / Change Request tracking system built with **Python** and **SQLite**.

This project was created as a mini portfolio project to demonstrate:
- working with a database (SQL)
- CRUD functionality (Create, Read, Update, Delete)
- input validation and clean CLI output
- structured code separation (UI / handlers / services)

## Features
- Create a change request (title + description)
- View all change requests
- View a request by ID
- Update request status (pending / approved / rejected)
- Delete a request with confirmation
- SQLite database persistence

## Tech Stack
- Python 3
- SQLite (Python standart library)

## Project Structure

```
change_tracker/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── services.py
│   ├── ui.py
│   └── handlers.py
├── .gitignore
├── change_tracker.db   (generated automatically when the app runs)
├── README.md
└── requirements.txt
```

## How to Run
1. Clone the repository
2. (Optional) Create and activate a virtual environment
3. Run:

#```bash
#py src/main.py

After starting application you will see a menu:

1. Add Change Request
2. View All Requests
3. View Request by ID
4. Update Request Status
5. Delete Request
6. Exit

Statuses allowed: pending, approved, rejected.

## Notes
The database file change_tracker.db is created automatically.
IDs don't reset after deletions (normal database behavior with autoincrement).
No external dependencies are required (standard Python library only).

## Future Improvements
Add unit tests
Add search/filter by status
Export requests to CSV


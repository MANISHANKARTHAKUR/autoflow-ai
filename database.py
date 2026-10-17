
import sqlite3

DB_NAME = "autoflow.db"


def get_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as conn:
        
        conn.execute("""
            CREATE TABLE IF NOT EXISTS execution_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER,
                action TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (task_id) REFERENCES tasks(id)
            )
        """)


def save_task(title, days_left, priority):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO tasks (title, days_left, priority)
            VALUES (?, ?, ?)
            """,
            (title, days_left, priority)
        )

        return cursor.lastrowid


def get_all_tasks():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM tasks ORDER BY id DESC"
        ).fetchall()

        return [dict(row) for row in rows]


def save_execution_log(task_id, action, result):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO execution_logs (task_id, action, result)
            VALUES (?, ?, ?)
            """,
            (task_id, action, result)
        )
        return cursor.lastrowid


def get_all_logs():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM execution_logs ORDER BY id DESC"
        ).fetchall()

        return [dict(row) for row in rows]

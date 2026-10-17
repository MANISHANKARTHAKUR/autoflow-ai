
from database import get_all_tasks


def check_deadlines():
    """Find pending tasks with approaching deadlines."""

    tasks = get_all_tasks()
    alerts = []

    for task in tasks:
        if task.get("status") != "pending":
            continue

        days_left = task.get("days_left", 999)

        if days_left < 0:
            message = "Deadline has passed"
        elif days_left <= 1:
            message = "Urgent: deadline is today or tomorrow"
        elif days_left <= 3:
            message = "Warning: deadline is approaching"
        else:
            continue

        alerts.append({
            "task_id": task["id"],
            "title": task["title"],
            "days_left": days_left,
            "alert": message
        })

    return alerts


def plan_task(title, days_left):
    if days_left < 0:
        return {
            "status": "invalid",
            "reason": "Days left cannot be negative"
        }

    if days_left <= 1:
        priority = "High"
        action = "Create urgent reminder"
    elif days_left <= 3:
        priority = "Medium"
        action = "Schedule reminder"
    else:
        priority = "Low"
        action = "Add to task list"

    return {
        "task": title,
        "priority": priority,
        "action": action
    }


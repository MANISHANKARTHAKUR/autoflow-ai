
def execute_action(task_id, title, action):
    # Execute a safe, local action.
    # For now, record the task as processed.
    return {
        "task_id": task_id,
        "task": title,
        "action": action,
        "result": "Action executed successfully"
    }


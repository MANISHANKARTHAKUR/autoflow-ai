
def verify_execution(execution):
    """Check whether an action result indicates success."""

    if not isinstance(execution, dict):
        return {
            "verified": False,
            "message": "Invalid execution data"
        }

    task_id = execution.get("task_id")
    result = execution.get("result")

    if task_id is None:
        return {
            "verified": False,
            "message": "Missing task ID"
        }

    if result != "Action executed successfully":
        return {
            "verified": False,
            "message": "Action execution was not successful"
        }

    return {
        "verified": True,
        "message": "Execution verified successfully"
    }

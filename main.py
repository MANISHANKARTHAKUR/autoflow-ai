
from agents.scheduler_agent import check_deadlines
from agents.verifier import verify_execution
from agents.action_agent import execute_action
from database import (
    initialize_database,
    save_task,
    get_all_tasks,
    save_execution_log,
    get_all_logs
)

from agents.planner import plan_task
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AutoFlow AI",
    description="A task automation API",
    version="1.0.0"
)
@app.on_event("startup")
def startup():
    initialize_database()

class Task(BaseModel):
    title: str
    days_left: int


@app.get("/")
def home():
    return {
        "message": "AutoFlow AI is running"
    }




@app.post("/automate")
def automate(task: Task):
    plan = plan_task(task.title, task.days_left)

    if plan.get("status") == "invalid":
        return plan

    task_id = save_task(
        task.title,
        task.days_left,
        plan["priority"]
    )

    execution = execute_action(
        task_id,
        task.title,
        plan["action"]
    )

    verification = verify_execution(execution)

    save_execution_log(
        task_id,
        execution["action"],
        execution["result"]
    )

    return {
        **plan,
        "task_id": task_id,
        "status": "saved",
        "execution": execution,
        "verification": verification
    }



@app.get("/tasks")
def list_tasks():
    return get_all_tasks()


@app.get("/logs")
def list_logs():
    return get_all_logs()

@app.get("/deadlines")
def monitor_deadlines():
    alerts = check_deadlines()

    return {
        "count": len(alerts),
        "alerts": alerts
    } 

@app.get("/health")
def health():
    return {"status": "healthy"}
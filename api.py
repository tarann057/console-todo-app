from fastapi import FastAPI, HTTPException
from tasks import add_task, get_tasks, delete_task

app = FastAPI()

@app.get("/tasks")
def read_tasks():
    return get_tasks()

@app.post("/tasks")
def create_task(task: str):
    add_task(task)
    return {"status": "ok"}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    try:
        delete_task(task_id)
        return {"status": "deleted"}
    except IndexError:
        raise HTTPException(404, "Task not found")

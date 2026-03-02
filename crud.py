from db import SessionLocal, Task

def add_task(description: str):
    db = SessionLocal()
    task = Task(description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task

def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks

def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        db.close()
        raise IndexError("No such task")
    db.delete(task)
    db.commit()
    db.close()
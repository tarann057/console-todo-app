tasks = []

def add_task(task: str):
    tasks.append(task)

def get_tasks():
    return tasks

def delete_task(index: int):
    if index < 0 or index >= len(tasks):
        raise IndexError("No such task")
    tasks.pop(index)

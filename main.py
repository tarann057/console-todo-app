from tasks import add_task, get_tasks, delete_task

def show_tasks():
    tasks = get_tasks()
    if not tasks:
        print("The task list is empty")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def menu():
    while True:
        choice = input("Choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            print("Task added")








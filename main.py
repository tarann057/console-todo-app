

tasks = []


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("The task has been added")

def show_tasks():
    if not tasks:
        print("The task list is empty")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number: "))
        if number < 1 or number > len(tasks):
            print("There is no such task")
            return

        tasks.pop(number - 1)
        print("The task has been deleted.")

    except ValueError:
        print("Enter the number")


def menu():
    while True:
        print("\nMenu:")
        print("1 - Add Task")
        print("2 - Show tasks")
        print("3 - Delete task")
        print("4 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
          add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Incorrect option")

menu()






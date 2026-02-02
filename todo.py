def show_menu():
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
        tasks.pop(task_number - 1)
        print("Task deleted successfully.")
    except:
        print("Invalid task number.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()

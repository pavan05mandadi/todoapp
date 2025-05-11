def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def delete_task(tasks, task_index):
    try:
        task_index = int(task_index) - 1
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted.")
    except IndexError:
        print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        print("Time")
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_index = input("Enter task number to delete: ")
            delete_task(tasks, task_index)
        elif choice == '4':
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
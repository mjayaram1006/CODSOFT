tasks = []

def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['name']} [{status}]")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        print("Task marked as done.")
    except:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

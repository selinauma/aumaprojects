# Student Planner App (Simple Version)

tasks = []

def add_task():
    title = input("Enter task title: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    
    task = {
        "title": title,
        "deadline": deadline,
        "completed": False
    }
    
    tasks.append(task)
    print("✅ Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    print("\n📚 Your Tasks:")
    for i, task in enumerate(tasks):
        status = "✔ Done" if task["completed"] else "❌ Not Done"
        print(f"{i+1}. {task['title']} | Deadline: {task['deadline']} | {status}")
    print()


def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!\n")
    except:
        print("Invalid input.\n")


def main():
    while True:
        print("====== STUDENT PLANNER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
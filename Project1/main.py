# this is a todo list using python
import os

def load_tasks(filename="todolist.txt"):    #function to load tasks
    if os.path.exists(filename):   
        with open(filename, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

def save_tasks(tasks, filename="todolist.txt"):  #function to save tasks
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):                # Function to add a new task
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' added to the list.")

def view_tasks(tasks):            # Function to view all tasks
    if tasks:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")

def remove_task(tasks):        # Function to remove a task
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def menu():                          # Main menu function
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose between 1-4.")

if __name__ == "__main__":
    menu()

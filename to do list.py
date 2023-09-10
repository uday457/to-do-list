# Create an empty list to store tasks
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view the tasks in the list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")
# Main loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

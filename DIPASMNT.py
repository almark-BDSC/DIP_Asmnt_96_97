import json # library to sasve and load tasks

# load tasks to file 
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return [] # If file does not exist, returm empty list
    
# Save tasks to file 
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file) 

# Add task
def add_tasks(tasks):
    task = input("Enter a tasks: ")
# Create a dictionary for task
    new_task = { 
        "task": task,
        "done": False
    }

    tasks.append(new_task)
    print("Task added")

# View Task 
def view_tasks(tasks):
    if len (tasks) ==0: # Check if the task list is empty
        print("No task found")

    else:
        number = 1

        for task in tasks:
            if task["done"] == True:
                status = "Done"
        else:
            status = "Not Done"
            print(str(number) + ". " + task["task"] + " - " + status)
            number = number + 1

# Edit task
def edit_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    number = int(input("Enter task number to edit: "))

    if number > 0 and number <= len(tasks):
        new_task = input("Enter new task name: ")
        tasks[number - 1]["task"] = new_task
        print("Task updated!")
    else:
        print("Invalid task number.")


# Remove task 
def remove_task(tasks):
    view_tasks(tasks)
    number = int(input("Enter task number to remove: "))

    if number > 0 and number <= len(tasks): # Check if number is valid
        tasks.pop(number - 1)
        print("Task remove")

    else:
        print("Invalid task number. ")

# Mark tasks as complete
def mark_task(tasks):
    view_tasks(tasks)
    number = int(input("Enter task number to mark complete: "))

    if number > 0 and number <= len(tasks): #Check if number is valid 

        tasks[number - 1]["done"] = True
        print("Task marked complete!")

    else:
        print("Invalid task number.")

# Main program 
tasks = load_tasks()
running = True

# Program loop
while running == True:
    print("\n========================")
    print("      TO-DO LIST")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Remove Task")
    print("4. Mark Task Complete")
    print("5. View Tasks")
    print("6. Save and Exit")

    choice = input("Choose option: ")

    # Run add task function
    if choice == "1":
        add_task(tasks)

    # Run remove task function
    elif choice == "2":
        remove_task(tasks)

    # Run mark task function
    elif choice == "3":
        mark_task(tasks)

    # Run view task function
    elif choice == "4":
        view_tasks(tasks)

    # Save and exit program
    elif choice == "5":
        save_tasks(tasks)
        print("Goodbye!")
        running = False

    # Invalid option
    else:
        print("Invalid choice.")
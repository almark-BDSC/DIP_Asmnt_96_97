import json # library to sasve and load tasks

# load tasks to file 
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []
    
# Save tasks to file 
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file) 

# Add task
def add_tasks(tasks):
    task = input("Enter a tasks: ")
     
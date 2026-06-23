import tkinter as tk 
from tkinter import messagebox 
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

# Refresh task list
def update_listbox():
    task_list.delete(0, tk.END)

    for task in tasks:
        if task["done"]:
            status = "Done"
        else:
            status = "Not Done"

        task_list.insert(tk.END, task["task"] + " - " + status)


# Add task
def add_task():
    task = task_entry.get()

    if task =="":
        messagebox.showerror("Error","Task cannot be empty.")
        return
    
    tasks.append({
    "task": task,
    "done": False
    })

    task_entry.delete(0, tk.END)
    update_listbox()
          

# Edit task
def edit_task(tasks):
    selected = task_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a task first.")
        return
    
    new_task = task_entry.get()

    if new_task =="":
        messagebox.showerror("Error", "Show a task name.")
        return 
    
    tasks[selected[0]]["task"] = new_task
    update_listbox()


# Remove task 
def remove_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a task first.")
        return
    
    tasks.pop(selected[0])
    update_listbox()

# Mark tasks as complete
def mark_task():
     selected = task_list.curselection()
     
     if not selected:
        messagebox.showerror("Error", "Select a task first.")
        return
     
     tasks[selected[0]]["done"] = True
     update_listbox()

# Save when X button is pressed
def save_exit():
    save_tasks(tasks)
    root.destroy()

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")

# Load tasks
tasks = load_tasks()

# Title
title = tk.Label(root, text="TO-DO LIST", font=("Arial", 18))
title.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=2)
tk.Button(root, text="Edit Task", command=edit_task).pack(pady=2)
tk.Button(root, text="Remove Task", command=remove_task).pack(pady=2)
tk.Button(root, text="Mark Complete", command=mark_task).pack(pady=2)
tk.Button(root, text="Save and Exit", command=save_tasks).pack(pady=10)

# Task list
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Task entry box
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Load tasks into listbox
update_listbox()

# Save if user clicks X
import tkinter as tk 
from tkinter import messagebox 
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

# Refresh task list
def update_listbox():
    task_list.delete(0, tk.END)

    for task in tasks:
        if task["done"]:
            status = "Done"
        else:
            status = "Not Done"

        task_list.insert(tk.END, task["task"] + " - " + status)


# Add task
def add_task():
    task = task_entry.get()

    if task =="":
        messagebox.showerror("Error","Task cannot be empty.")
        return
    
    tasks.append({
    "task": task,
    "done": False
    })

    task_entry.delete(0, tk.END)
    update_listbox()
          

# Edit task
def edit_task(tasks):
    selected = task_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a task first.")
        return
    
    new_task = task_entry.get()

    if new_task =="":
        messagebox.showerror("Error", "Show a task name.")
        return 
    
    tasks[selected[0]]["task"] = new_task
    update_listbox()


# Remove task 
def remove_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a task first.")
        return
    
    tasks.pop(selected[0])
    update_listbox()

# Mark tasks as complete
def mark_task():
     selected = task_list.curselection()
     
     if not selected:
        messagebox.showerror("Error", "Select a task first.")
        return
     
     tasks[selected[0]]["done"] = True
     update_listbox()

# Save when X button is pressed
def save_exit():
    save_tasks(tasks)
    root.destroy()

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")

# Load tasks
tasks = load_tasks()

# Title
title = tk.Label(root, text="TO-DO LIST", font=("Arial", 18))
title.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=2)
tk.Button(root, text="Edit Task", command=edit_task).pack(pady=2)
tk.Button(root, text="Remove Task", command=remove_task).pack(pady=2)
tk.Button(root, text="Mark Complete", command=mark_task).pack(pady=2)
tk.Button(root, text="Save and Exit", command=save_tasks).pack(pady=10)

# Task entry box
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Task list
task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

# Load tasks into listbox
update_listbox()

# Save if user clicks X
root.protocol("WM_DELETE_WINDOW", save_exit)

# Run program
root.mainloop()

# Run program
root.mainloop()
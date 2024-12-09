from datetime import datetime

def load_password():#Load password from .txt file
    with open('password.txt', 'r') as f:
        return f.read().strip()
    
def login():#Allow user to login with password
    stored_password = load_password()
    while True:
        user_input = input("Enter your password: ")
        if user_input == stored_password:
            print("Login successful!")
            break
        else:
            print("Incorrect password. Try again")

def add_task():#Add a task to the .txt file
    task_name = input("Enter task name: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    category = input("Enter category: ")
    status = "Pending"
    with open('tasks.txt', 'a') as f:
        f.write(f"{task_name}|{deadline}|{category}|{status}\n")
    print("Tasks added succesfully!")

def view_tasks():#View tasks in .txt file
    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks found!")
            else:
                for idx, task in enumerate(tasks, 1):
                    task_name, deadline, category, status = task.strip().split('|')
                    print(f"{idx}. {task_name} | Deadline: {deadline} | Category: {category} | Status: {status}")
    except FileNotFoundError:
            print("No tasks file found! Add a task first.")

def complete_task():#Allows ticking off of tasks for completion
    view_tasks()
    task_no= int(input("Enter the task number to mark as compelted: "))
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    tasks[task_no - 1] = tasks[task_no - 1].replace("Pending", "Compelted")
    with open('tasks.txt', 'w') as f:
        f.writelines(tasks)
        print("Task marked as completed!")

def delete_task():
    view_tasks()
    task_no = int(input("Enter the task number to delete: "))
    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()
    del tasks[task_no - 1]
    with open('tasks.txt', 'w') as f:
        f.writelines(tasks)
    print("Task deleted succesfully!")

def check_deadlines():
    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()
            today = datetime.now().date()
            for task in tasks:
                task_name, deadline, category, status = task.strip().split('|')
                deadline_date = datetime.strp(deadline, "%Y-%m-%d").date()
                days_left = (deadline_date - today).days
                if days_left <= 2 and status == "Pending":
                    print(f"Reminder: '{task_name}' is due in {days_left} day(s)!")
    except FileNotFoundError:
        print("No tasks to check deadlines.")

if __name__ == "__main__":
    complete_task()
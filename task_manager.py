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
        today = datetime.today().date()  # Get today's date
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

        if not tasks:
            print("No tasks to check deadlines for.")
        else:
            for task in tasks:
                task_name, deadline, category, status = task.strip().split('|')
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()  # Parse the deadline string
                days_left = (deadline_date - today).days

                if days_left < 0:
                    print(f"Task '{task_name}' is overdue! Deadline was {deadline_date}.")
                elif days_left == 0:
                    print(f"Task '{task_name}' is due today!")
                else:
                    print(f"Task '{task_name}' has {days_left} days left. Deadline: {deadline_date}.")
    except FileNotFoundError:
        print("No tasks file found. Please add tasks first.")
    except ValueError as e:
        print(f"Error processing tasks: {e}")



def main():
    while True:
        print("\nTask Manager")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Check Deadlines")
        print("6. Quit")
        choice = input("Choose an Option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            check_deadlines()
        elif choice == '6':
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    login()
    main()

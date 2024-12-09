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

def add_task():
    task_name = input("Enter task name: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    category = input("Enter category: ")
    status = "Pending"
    with open('tasks.txt', 'a') as f:
        f.write(f"{task_name}|{deadline}|{category}|{status}\n")
    print("Tasks added succesfully!")

if __name__ == "__main__":
    add_task()
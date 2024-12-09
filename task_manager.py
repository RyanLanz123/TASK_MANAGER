def load_password():#Load password from .txt file
    with open('password.text', 'r') as f:
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
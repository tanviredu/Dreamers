# Dictionary to store usernames and passwords (for demonstration purposes)
credentials = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and if the password matches
    if username in credentials and credentials[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Main function to run the login project
def main():
    print("Welcome to Simple Login System")
    while True:
        choice = input("Enter 'login' to proceed or 'exit' to quit: ")
        if choice.lower() == 'login':
            login()
        elif choice.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'login' or 'exit'.")

if __name__ == "__main__":
    main()




def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Check if all criteria are met
    if has_uppercase and has_lowercase and has_digit:
        return True, "Password is strong."
    else:
        return False, "Password must contain at least one uppercase letter, one lowercase letter, and one digit."



print("Enter password")
passwrod = input()
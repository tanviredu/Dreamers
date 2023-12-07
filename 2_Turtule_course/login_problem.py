def login(username, password):
    # Sample username and password for demonstration
    valid_username = "user123"
    valid_password = "password123"

    if username == valid_username and password == valid_password:
        return "Login successful!"
    else:
        return "Login failed. Invalid username or password."

# Example
username_input = input("Enter username: ")
password_input = input("Enter password: ")

login_result = login(username_input, password_input)
print(login_result)

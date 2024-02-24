
def print_pattern(rows):
    for i in range(1, rows + 1):
        print("* " * i)

# Example
num_rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(num_rows)


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Assuming a hardcoded username and password for demonstration purposes
    correct_username = "student123"
    correct_password = "password123"

    attempts = 0
    max_attempts = 3

    while True:
        if username == correct_username and password == correct_password:
            print("Login successful!")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Incorrect username or password. Please try again.")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
            else:
                print("Too many incorrect attempts. Your account is locked.")
                break

login()
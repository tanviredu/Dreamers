def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# User input for operation and operands
operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation"

# Display the result
print(f"Result: {result}")

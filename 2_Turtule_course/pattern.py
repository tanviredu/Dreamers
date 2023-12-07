Copy code
def print_pattern(rows):
    for i in range(1, rows + 1):
        print("* " * i)

# Example
num_rows = int(input("Enter the number of rows for the pattern: "))
print_pattern(num_rows)

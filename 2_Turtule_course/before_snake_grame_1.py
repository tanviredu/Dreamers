# Function to find grades depending on the mark
def find_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Function to convert meter to kilometer
def meter_to_kilometer(meter):
    return meter / 1000

# Function to convert centimeter to meter
def cm_to_meter(cm):
    return cm / 100

# Function to calculate the sum of n numbers
def sum_of_n_numbers(n):
    return sum(range(1, n+1))

# Function to print the pattern using loop
def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usages
mark = 85
grade = find_grade(mark)
print("Grade for mark", mark, "is:", grade)

meter = 5000
kilometer = meter_to_kilometer(meter)
print(meter, "meters is equal to", kilometer, "kilometers")

cm = 200
meter = cm_to_meter(cm)
print(cm, "centimeters is equal to", meter, "meters")

n = 10
sum_n = sum_of_n_numbers(n)
print("Sum of first", n, "numbers is:", sum_n)

rows = 5
print_pattern(rows)

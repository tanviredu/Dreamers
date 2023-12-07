def mark_to_grade(mark):
    if 0 <= mark <= 100:
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
    else:
        return "Invalid mark. Mark should be between 0 and 100."

# Example
student_mark = float(input("Enter the student's mark: "))
grade = mark_to_grade(student_mark)
print(f"The student's grade is: {grade}")
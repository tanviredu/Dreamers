def first_half_of_even_string(input_string):
    if len(input_string) % 2 == 0:
        half_length = len(input_string) // 2
        return input_string[:half_length]
    else:
        return "Input string length is not even."

# Example
input_str = "PythonIsCool"
result = first_half_of_even_string(input_str)
print("Result:", result)

# Find the length of a string
def find_length(input_string):
    length = len(input_string)
    return length

# Convert a string to lower case
def convert_to_lower(input_string):
    lower_case_string = input_string.lower()
    return lower_case_string

# Convert a string to upper case
def convert_to_upper(input_string):
    upper_case_string = input_string.upper()
    return upper_case_string

# Find a specific character in a string
def find_character(input_string, char):
    index = input_string.find(char)
    return index

# Find the number of times a specific character occurs in a string
def count_character_occurrences(input_string, char):
    count = input_string.count(char)
    return count

# Replace a specific character in a string
def replace_character(input_string, old_char, new_char):
    replaced_string = input_string.replace(old_char, new_char)
    return replaced_string

# Reverse a string
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage
input_str = "Hello, World!"

print("Length of the string:", find_length(input_str))
print("String in lower case:", convert_to_lower(input_str))
print("String in upper case:", convert_to_upper(input_str))

char_to_find = "o"
print(f"Index of '{char_to_find}':", find_character(input_str, char_to_find))
print(f"Number of occurrences of '{char_to_find}':", count_character_occurrences(input_str, char_to_find))

old_char = "o"
new_char = "X"
print(f"String after replacing '{old_char}' with '{new_char}':", replace_character(input_str, old_char, new_char))

print("Reversed string:", reverse_string(input_str))

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive palindrome check
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_str = "A man a plan a canal Panasma"

if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")

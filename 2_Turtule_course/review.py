def sum_of_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def reverse_string(s):
    return s[::-1]

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        return None
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])
    return result

# Test the functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of even numbers:", sum_of_even(numbers))

string = "hello"
print("Reversed string:", reverse_string(string))

numbers_with_duplicates = [1, 2, 3, 4, 2, 3, 5, 6, 1]
print("List with duplicates removed:", remove_duplicates(numbers_with_duplicates))

test_list = [3, 7, 2, 10, 5]
print("Maximum value in list:", find_max(test_list))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print("Result of multiplying lists element-wise:", multiply_lists(list1, list2))


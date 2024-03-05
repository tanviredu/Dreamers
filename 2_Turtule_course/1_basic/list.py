

my_list = [1, 2, 3, 4, 5]

# Append a new element to the end of the list
new_element = 6
my_list.append(new_element)

print(my_list)  # Output: [1, 2, 3, 4, 5, 6]





my_list = [1, 2, 3, 4, 5]

# Remove a specific value
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]

# Remove by index
index_to_remove = 2
del my_list[index_to_remove]
print(my_list)  # Output: [1, 2, 5]


my_list = [1, 2, 3, 4, 5]

# Check if an item exists
item_to_check = 3
if item_to_check in my_list:
    print(f"{item_to_check} is in the list.")
else:
    print(f"{item_to_check} is not in the list.")

my_list = [1, 2, 3, 4, 5]

# Get the length of the list
length_of_list = len(my_list)
print(f"The length of the list is {length_of_list}.")



my_list = [1, 2, 2, 3, 4, 2, 5]

# Count occurrences of a specific value
count_of_2 = my_list.count(2)
print(f"The count of 2 in the list is {count_of_2}.")


my_list = [1, 2, 3, 4, 5]

# Access elements using a for loop
for item in my_list:
    print(item)


my_list = [1, 7, 3, 9, 5]

# Find the maximum value
max_value = max(my_list)
print(f"The maximum value in the list is {max_value}.")



my_list = [1, 7, 3, 9, 5]

# Find the minimum value
min_value = min(my_list)
print(f"The minimum value in the list is {min_value}.")
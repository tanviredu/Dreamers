my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_odd = 0
for num in my_list:
    if num % 2 != 0:
        sum_odd += num

print("Sum of odd values:", sum_odd)

sum_even = 0
for num in my_list:
    if num % 2 == 0:
        sum_even += num

print("Sum of even values:", sum_even)

total = 0
for num in my_list:
    total += num

average = total / len(my_list)
print("Average:", average)

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)


my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

6. Difference between list, tuple, set:
List: Ordered, mutable (can be changed), allows duplicate elements.
Tuple: Ordered, immutable (cannot be changed), allows duplicate elements.
Set: Unordered, mutable, does not allow duplicate elements.
Here's a brief summary of the differences:

Lists are ordered and can contain duplicate elements.
Tuples are ordered and immutable.
Sets are unordered and do not allow duplicates.
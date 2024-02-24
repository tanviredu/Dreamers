# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])  # Output: John

# Adding a new key-value pair
my_dict['gender'] = 'Male'

# Updating an existing value
my_dict['age'] = 26

# Removing a key-value pair
del my_dict['city']

# Checking if a key exists
if 'name' in my_dict:
    print('Key "name" exists in the dictionary.')

# Getting all keys and values
all_keys = my_dict.keys()
all_values = my_dict.values()

# Getting all key-value pairs
all_items = my_dict.items()

# Clearing the dictionary
my_dict.clear()

# Creating a copy of the dictionary
new_dict = my_dict.copy()

# Example of dictionary after operations
print("Updated Dictionary:", new_dict)

# Initializing a dictionary with different data types
mixed_dict = {'name': 'Alice', 'age': 30, 'grades': [90, 85, 88], 'is_student': True}

# Accessing values with different data types
print("Name:", mixed_dict['name'])
print("Grades:", mixed_dict['grades'][0])
print("Is Student?", mixed_dict['is_student'])

# Example of nested dictionaries
nested_dict = {'person': {'name': 'Bob', 'age': 28, 'city': 'London'}}

# Accessing values in nested dictionaries
print("Person's Name:", nested_dict['person']['name'])





# Creating sets
set1 = {1, 2, 3}
set2 = set([2, 3, 4])



x = {
  "zarif_user":"zarif123",
  "zarif_pass":"123456",
  "ratib_user":"ratib100",
  "ratib_pass":"23456"
}


#print(x["zarif_user"])
#print(x["zarif_pass"])

ratib = {
  "FullName": "Ratib sikdar",
  "age":12,
  "city":"Dhaka",
  "class":7
}

ratib['city'] = "Chittagong"
ratib['age'] = 13

#print(ratib['city'])
#print(ratib['age'])

""
#10,20,30,40,50
zarif_score = {
  "name":"Zarif Zawad",
  "score": [10,20,30,40,50]
}

#print(zarif_score['score'])

mylist = [1,2,3,100,200,300]

#for item in mylist:
#  print(item)



mydict = {
  "name1": "Tanvir",
  "name2": "Zarif",
  "name3": "Ratib",
  "age1":30,
  "age2": 12,
  "age3":15
}


#for x,y in mydict.items():
#  print(x,y)


x = {
  "zarif_user":"zarif123",
  "zarif_pass":"123456",
  "ratib_user":"ratib100",
  "ratib_pass":"23456"
}

#if 'zarif_pass' in x:
#  print("yes password ache")
#else:
#  print("password nei")

y = x.copy()

#print(y)

my_key = x.keys()
my_values = x.values()

#print(my_key)
#print(my_values)


mylist = [1,2,3,4,5,5,5,6,7,7]
myset = set(mylist)
print(myset)


di = {1,2,3,4,5,5,5}
di.add(6)
di.add(5)
di.remove(1)
print(di)











# Adding an element to a set
set1.add(4)

# Removing elements from a set
set1.remove(2)
set1.discard(3)
popped_element = set1.pop()
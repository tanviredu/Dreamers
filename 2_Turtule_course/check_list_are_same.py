def check_list_same_or_not(list1,list2):
    is_same = sorted(list1) == sorted(list2)
    return is_same

a = [1,2,3,4,5,6]
b = [6,5,4,3,2,2]

if check_list_same_or_not(a,b):
    print("The List are equal")
else:
    print("The List are not equal")


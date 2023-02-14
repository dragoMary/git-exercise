
'''
# Exercise 1: Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)                       # by slicing

# Exercise 2: Access value 20 from the tuple
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
n = tuple2[1][1]
print(n)


#  Create a tuple with single item 50
tuple = (50,)
print(tuple)

# Unpack the tuple into 4 variables
tuple3 = (10, 20, 30, 40)
a, b, c, d = tuple3
print(a)
print(b)
print(c)
print(d)

# Exercise 5: Swap two tuples in Python
tuple_1 = (11, 22)
tuple_2 = (99, 88)
swap = tuple_1
tuple_1 = tuple_2
tuple_2 = swap
print(tuple_1)
print(tuple_2)

# Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple6 = (11, [22, 33], 44, 55)
tuple6[1][0] = 222
print(tuple6)

# Write a Python function that takes two lists and returns True if they have at least one common item.

def check_lists(list1: list, list2: list) -> bool:
    return set(list1).intersection(list2)

list1 = [list]
list2 = [list]

if check_lists(list1, list2):
    print(True)
else:
    print(False)

'''

# Exercise 8:
# Write a Python function to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
# NOTE: Items in given string can be str, int, float NOT list, tuple, set or dictionary

def insert_to_list():
    sample_list = [1, 2, 3, 4]
    string = "emp"
    new_list = []
    for i, number in enumerate(sample_list, 1):
        new_item = f"{string}{i}"
        new_list.insert(i - 1, new_item)
    return new_list

print(insert_to_list())
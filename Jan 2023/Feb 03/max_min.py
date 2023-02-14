
'''
a = [1, 109, 45, 67, 3]
#print(max(a))
#print(min(a))
#print(sum(a))


#b = ['A', 'b', 'E', 'z']
#print(max(b))
#print(min(b))

sorted_num = sorted(a)
print(sorted_num)

my_dict = {'a': 4, 'c': 2, 'b': 89}
my_var = sorted(my_dict.values(), reverse=True)
print(my_var)
#print(sorted(my_dict))


list1= [
{'name': 'john', 'age': 45},
{'name': 'mary', 'age': 18},
{'name': 'bob', 'age': 25}

]
by_age = lambda profile: profile['age']
# lambda instead def, profile as parameter and profile['age'] instead return profile['age']

by_name = lambda profile: ['name']
#print(by_age)    # returns where is stored in memory
for i in list1:
    print(by_age(i))    # print just the age

print(sorted(list1, key=by_age)) # for each name output its age

print(sorted(list1, key=by_name))  # sort by asking table

a_list = [1, 'Julia', {2, 4}]    # here boolians. so, 0 , empty list, empty string is false by default
print(any(a_list), all(a_list))
a_list = [0,  'Julia', {2, 4}]
print(any(a_list), all(a_list))
'''

a_list = [1, 2, 3, 4, 5]
by_two = lambda num: num * 2   # result of this is stored in a list.
mult_list = map(by_two, a_list)    #map return object
print(mult_list)    # return teh storage in memory
print(list(mult_list))


is_odd = lambda num: (num % 2) != 0
odds = filter(is_odd, a_list)
print(odds)
print(list(odds))
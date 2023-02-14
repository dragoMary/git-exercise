my_dict = {
    'name': 'Julia',
    'adress': 'CC street',      # all this are keys
     'age': 36,
    'language': ['english', 'german', 'french']

}
print(my_dict['name'])
print(my_dict.get('age'))

template_dict = dict.fromkeys(['name', 'age', 'topics'], 'not created')
#print(template_dict)

my_dict.setdefault('pet', 'cat')
print(my_dict)
print(my_dict['language'][2])

dict_to_merge = {
    'name': 'Olga',
    'age': 18,
    'country': 'germany'
}

my_dict.update(dict_to_merge)
print(my_dict)

print(my_dict.popitem())   #remove item from end of dict
print(my_dict)

b = my_dict.pop('name')
print(b)
print(my_dict)

new_dict = my_dict.copy()
print(new_dict)
new_dict.clear()

a = my_dict.keys()
my_values = my_dict.values()
my_items = my_dict.items
print(my_values)


for key, values in my_dict.items():
    print(key)                       # 'items' print a tuple

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {1: 'a', 3: 'c', 2:'b'}
print(dict1==dict2)

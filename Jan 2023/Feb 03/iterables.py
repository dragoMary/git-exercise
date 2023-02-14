my_list = ['Maria', 'Bob', 'Davis', 'Michael']
#for item in my_list:
    #print(item)

#for i in range(len(my_list)):      # we get the index of each name
    #print(i)
    #print(my_list[i])

my_dict = {
    'name' : 'Bob',
    'age' : 15,
    'country': 'Germany'
}
#for item in my_dict:
    #print(my_dict[item])      # print the item(key) + its value
    #print(item)

#for key in my_dict.keys():
    #print(key)
for x in my_dict.values():    # print the values
    print(x)

for key, value in my_dict.items():     # print keys + its values
    print(key, '->', value)


days = {
    ('mon', 'monday'),
    ('tue', 'tuesday'),

}

for x, y in days:
    print(x, 'is', y)
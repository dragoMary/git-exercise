'''
days_list = ['monday', 'tuesday', 'thursday']
# i can specify with what nr to start if i want, ansonst start from 0 and i take off 11
for index, value in enumerate(days_list, 11):
    print(index, '->', value)

position = 0
for item in days_list:
    print(position, '->', item)
    position += 1

# here we put the exemple_dict whatever{}
#for index, (key, value) in enumerate(exemple_dict.items())
    #print(index, '=', key, '->', value)

'''
numbers = [1, 2, 3]
str_num = ('one', 'two', 'tree')
num_dict = {'a': 1, 'b': 2, 'c': 3}
set_num = {'one', 'two', 'tree'}
zip_var = zip(numbers, str_num, num_dict, set_num)
for i in zip_var:
    print(i)



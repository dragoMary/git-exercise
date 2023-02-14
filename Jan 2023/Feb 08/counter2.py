
from collections import Counter, OrderedDict, ChainMap, namedtuple

fridge = ['Apple', 'Apple', 'Cabbage', 'Steak', 'Cheese', 'Apple', 'Carrot', 'Carrot', 'Yogurt', 'Beer']
my_count = Counter(fridge)
#print(my_count.total())

lunch = Counter(Apple=2, Steak=1)
my_count.subtract(lunch)
#print(my_count)

shopping = Counter(Flowers=3, Banana=5)
my_count.update(shopping)
print(my_count)
#for item in my_count :
 # print(item)

count1 = Counter(Apple=3, Banana=2)
count2 = Counter(Banana=1, Cheese=3)
print(count1 + count2)
print(count1 & count2)
print(count1 | count2)   #or
print(count1==count2)
print(count1!=count2)


my_dict = {
    'name': 'Bob',
    'age': 56,
    'country': 'Germany'
}

my_ordered_dict = OrderedDict(my_dict)
print(my_ordered_dict['name'])
my_ordered_dict.move_to_end('age', last=False)
print (my_ordered_dict)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6, 'a': 1}
for item1, key in dict1.items():
    for key1, value1 in dict2.items():
        if key == key1:
            sum_dict[key] = value + value1
        #else:
            #sum_dict[key] =
            print(sum(dict))
chain = ChainMap(dict1, dict2)
#print(chain)
#print(dict(chain))

#dict1.update(dict2)
#print(dict1)
#print(chain.maps)
#print(chain.maps[1]['a'])
#print(chain['a'])

my_address = namedtuple('Address', ['street', 'number', 'city', 'country'])
home = my_address('bla-bla street', 13, 'Berlin', 'Germany')
print(home)
print(home[0])
print(home.country)
#home.city = 'Hamburg'  #tuple cant be changed
#print(home._asdict())
print(id(home))
new_home = home._replace(number=6)
home = home._replace(number=6)  # print a new id
#print(new_home)
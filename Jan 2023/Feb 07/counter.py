fridge = ['apple', 'apple', 'cabbage', 'steak', 'cheese', 'apple', 'carrot', 'carrot', 'yogurt']
counter = {}
for ingredient in fridge:
    if ingredient in counter:
        counter[ingredient] +=1
    else:
        counter[ingredient] = 1
#print(counter)

from collections import Counter
my_counter = Counter(fridge)
print(my_counter)
print(my_counter.total())

lunch = Counter(carrot=1, cabbage=1)
#print(lunch)
#my_counter.update(lunch)
#print(my_counter)

#print(my_counter.most_common())
print(my_counter.subtract(lunch))
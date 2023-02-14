'''
from collections import defaultdict

integer = defaultdict(int)
integer['1'] = 33
integer['2'] = 44

print(integer['3'])
#The code above outputs 0 since it is the default integer.

import collections

K = collections.OrderedDict()
K['Value1'] = 29
K['Value2'] = 30
K['Value3'] = 33
K['Value4'] = 44


for x,y in K.items():
    print (x,y)


from collections import deque

list = ["a","b","c","d"]
letter = deque(list)

print(letter)

#A deque, pronounced “deck”, is a list designed to make it simple to add and remove items.

'''
from collections import Counter

list = [1,2,4,7,5,1,6,7,6,9,1]
K = Counter(list)
print(K)
print(K[7])
# above it is counted how many times 7 appear in list and how many times each int app in list

import collections
value = collections.defaultdict(lambda : 'Key is missing')
value['x'] = 1
value['y'] = 2

print ("The monetary value attached to 'x' is : ",end="")
print (value['x'])
print ("The monetary value attached to 'k' is : ",end="")
print (value['k'])


dct = {'a': 1, 'b': 12}
for i in dct:               # itereza doar litera
    print(i)
for i in dct.values():      # itereaza doar valoarea asociata literei
    print(i)
for k, v in dct.items():    # itereaza atat litera cat si valoarea ei
    print(k, v)

print(hasattr(3.14, '__iter__'))        # se verifica daca un obiect este iterabil sau nu
print(hasattr('pi', '__iter__'))
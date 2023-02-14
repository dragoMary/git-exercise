
'''

my_set = {'String', 2, 'String', (True, 2, None), 'String', (True, 2, None), None, 'string'}
set_f_str = set('hello')
empty_set = set()
new_set = my_set.copy()
print(new_set)
print(my_set)
#print(my_set[2])    # set dont support index

set_f_str.add((True, None))
print(set_f_str)

set_f_str.update(['2', 2, 2.87])
print(set_f_str)

set_f_str.discard('H')
print(set_f_str)
'''
test_set = {True, 3, 7, None}
print(test_set)
test_set.clear()

fruits = {'pear', 'mango', 'apple', 'stawberry'}
smoothie = {'mango', 'orange', 'pear'}
print (fruits.intersection(smoothie))   # fructele comune in cele doua seturi
print (fruits.symmetric_difference(smoothie))  # fructele diferite in cele doua seturi

d = fruits.difference(smoothie)  # diferenta doar in main set
e = smoothie.difference(fruits)
#print(d)
#print(e)

#a = fruit
# intersection_update(smoothie)
#print(a)
#print(fruits)

#fruits.symmetric_difference_update(smoothie)
#print(fruits)

#union_set = fruits.union(smoothie) #  returneaza toate fructele , mai putin cele duplicat
#print(union_set)
print(fruits.isdisjoint(smoothie)) # returneaza fals pt ca elementele au aceeasi valoare.
                                    #dar poate returna True daca pe langa fructe apar elemente care nu definesc un fruct

sub_set = {'mango', 'pear'}
#print(fruits.issubset(sub_set))
#print(sub_set.issubset(fruits))

set1 ={1, 2, 3}
set2 = {3, 1, 2}
print(set1==set2)
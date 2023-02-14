my_list = ['string', 2, True, [1, 'A', 2.45], 7.987]
var1 = 'hello world'
var2 = 'extra'
list_from_string = list(f'{var1}{var2}')
#list_from_string = list('hello world' + 'extra')  # other version of calling the list
#print(list_from_string)

int_list = list(range(1,10,2))
print(int_list)

print(my_list[1:4])
print(my_list[::-1])
fruits = ['banana', 'apple', 'grape', 'orange', 'grape']
print(fruits.index('apple'))    # position in list
print(fruits.index('grape', 3))  #positio 4
print(fruits.count('grape'))       #appears 2 times in list

print(fruits[::-1])  #listeaza reversul listei
print(fruits)       # listeata fructele in original position

fruits.reverse()
print(fruits)

int_list1 = [2, 98, 5, 109, 0]
#int_list1.sort(reverse=True)
#print(int_list)


#fruits.sort()
#print(fruits)

#fruits[0] = 'bla-bla'
#print(fruits)

#fruits[1:3] = ['some string']
#print(fruits)

berries = ['strawberrys', 'blueberry']
fruits = fruits + berries
print(fruits)
fruits.extend(berries)
print(fruits)
fruits.insert(1, 'papaya')  # 1st place is taken by papaya
print(fruits)

first_item = fruits.pop(3)
print(first_item)
print(fruits)



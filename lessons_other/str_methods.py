
'''
my_string =  'this is my string'
print(id(my_string))
print(my_string.split('s')) #scoate afara litera s din orice cuvant din lista

print(my_string.split('s', '#'))  #inlocuieste s cu #
print(id(my_string))

my_string = my_string.replace('s', '#')
print(my_string)
print(id(my_string))


print(my_string.count('s'))

print(my_string.strip('#'))  # cleant it up with #

print(my_string.rstrip('#'))  # clean de la dreapta
print(my_string.lstrip('#'))  # de la stanga

print(my_string.startwith('jul'))
print(my_string.endtwith('jul'))
print(my_string.centerwith(40, '*'))
print(my_string.ljust(40, '*'))
print(my_string.rjust(40, '*'))

my_string = 'HelloW, WoRld'
other_string = 'World'
print(my_string + other_string)
print(my_string * other_string)  # multiplica de 3 ori
# varianta 1
user = input('enter your name ')
my_string = 'Hello {}' . format(user)   # curly brackets print the variable (numele userului) daca punem .format('user')
my_string = 'Hello {}' , you are {}. format(name='Julia', age='36')


# varianta2
name = 'Julia'
age = 36
my_string = f'Hello {name.upper()}', you are {age}'. format(name='Julia', age= '36')          # f vine de la formating
print(my_string)


for i in range(len(my_string)):
    print(my_string[i])           # i reprezint index


for char in my_string[]:
        print(char)



from timeit import default_timer as timer
my_list = ['a'] * 10
start = timer()
my_string = ''
for i in my_list:
  my_string += i   # concat

end = timer()
print('with + {end -start}')

start = timer()

b = ''.join(my_list)
end = timer()
print(f'with join() {end - start}')
print(my_string == my_string2)


a = ['hello, ' ', 'world]
b = ['hello' + '' +  'world']    # b = ''.join(a)
print(b)

'''

from timeit import default_timer as timer

a = ['a'] *10
start = timer()
a =  ''    #empty string
for i in a:
    a += i
end = timer()
print(f'with + {end - start}')


start = timer()
my_string2 = ''.join(a)
end = timer()
print(f'with {end - start}')


#print(txt.splitlines())





'''             # Task 1 - basic math operations
for i in range(2):
    number = input('enter a number:')

    if int(number) % 2 == 0:
        print('the number is even.')
    else:
        print('the number is odd.')


    number = input('Enter a number:')

    if int(number) % 2 == 0:
        print('the number is even.')
    else:
        print('the number is odd.')
'''



'''
number = input('Enter a number:')

if int(number) % 2 == 0:
    print('the number is even.')
else:
    print('the number is odd.')

'''

'''
y = 2
while y > 0:
    print('python!' * y)
    y-= 1
'''

'''
x = 10          # comparison operators (boolean)
y = 50
print (x > y)
print (x < y)

'''

'''
x = 75    # assignment operators
y = 25
# x = x + y
x +=y
print(x)

'''


'''
x = -75     # logical operators
y = 25


if x > 0 and y > 0:
    print('the numbers are greater than 0')
else:
    print('at least one number is not greater than 0')



x = 75
y = 25
z = -10

if x and y and z:
    print('Atleast one number has boolean value as True')
else:
    print('All the numbers have boolean value as False')

'''

'''

x = 11
if not x:
    print("Boolean value of a is True")

if not (x % 3 == 0 or x % 5 == 0):
    print("x is not divisible by either  3 or 5")
else:
    print("x is divisible by either 3 or 5")

'''

'''
# loop *3

for x in range(3):
    number = input('enter a number:')

    if int(number) % 2 == 0:
        print('the number is even.')
    else:
        print('the number is odd.')

'''
'''                
i = 0          # (ex. with while)
while i < 3:
        num = int (input ('enter a number:'))
        i = i + 1
        if  (num % 2) == 0:
           print('the number is even')
        else:
           print('the number is odd')
'''
'''
# Task 2 - printing numbers with `range()` function
i = 0
while i < 4:
     i = i + 1

     num = int(input('enter a number:'))
     if num == 1:
          num = int(input('enter another number:'))
     for x in range(num):
          if num == 2: continue
          if num == 3: continue
          print(x)
     if num == 2:
          start = int(input('starting number:'))
          stop = int(input('stopping number:'))
          for x in range(start, stop):
               print(x)

     if num == 3:
          start = int(input('starting number:'))
          stop = int(input('stopping number:'))
          step = int(input('step:'))
          for x in range(start, stop, step):
               print(x)
'''

'''
# Task 3 - finding divisors of a number

num = int(input('enter a number:'))
for y in range(2, num+1):
  if num % y == 0:
        print(y)
'''
'''
# Task 4 - check prime number

num = int(input('enter a number:'))
if num > 1:
    for x in range(2, int(num/2) +1):
        if (num % x) == 0:
            print(num, 'is NOT a prime number')
            break
    else:
        print(num, 'is a prime number')
'''
'''
# Task 5 - FizzBuzz

for x in range(1, 100):
    if x % 3 ==0 and x % 5 ==0:
        print('FizzBuzz')
        continue
    if x % 3 ==0:
        print('Fizz')
        if x % 3 == 0:
            continue

    if x % 5 ==0:
        print('Buzz')
    else:
        print(x)
'''
'''
# Task 6 - divisible numbers

for x in range(1000, 2000):
    if x % 7 == 0 and x % 5 != 0:
        print(x)

'''






#TASK1
'''
three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5
three_five_mul = three_mul + five_mul
for i in range(1, 100):

    if i%num1 == 0 and i%num2 == 0:
        print(i, three_five_mul)
    elif i%num1 == 0:
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)

'''

#TASK2
'''
n = 5
number = 1
sum = 10
while number < n + 1:
    sum = sum + 1
    number = number + 1
print('sum = ', sum)

'''

#TASK3
'''
n = 5
sum = 5
for num in range(n):
    sum += num
print("Sum =", sum)

'''

#TASK4
'''
for x in range(3):
    print(x)



for j in range(5):
    print('This is loop number ',j)


x = 10
while x > 0:
        print(x)
        x -= 1


countdown = 6
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")
    
'''
'''
result = 0

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

if x == y or y == z:

    print("Calculated sum is ", result)

else:
   sum = x + y + z
   print ("Calculated sum is ", sum)

'''
'''
x = int(input("First number: "))
y = int(input("Second number: "))
result = x + y
sum = 20
if (result) < 15 or (result) < 20:
    print("Calculated sum is ", sum)
else:
    print("Calculated sum is ", result)

'''

'''
#TASK7

a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, ", b = ", b)

temp = a, b
a, b = b, a

print("After swapping: a =", a, " ,b =", b)

'''
'''
#TASK8


x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))

'''

#TASK9          partial solved
'''
x = input("Type your value: ")

if x == '0':
    x = False
elif x == '1':
    x = True
else:
    pass

print("Your entered value is now ", x)

'''
#TASK10

'''

x = int (input ('Enter first number: '))

y = int (input ('Enter second number: '))

if x%y == 0:

              print ('First number is divisible with second number.', float(x/y))

elif y%x == 0:

              print ('Second number is divisible with first number.', float(y/x))
else:

              print ('The numbers are not divisible.')
'''
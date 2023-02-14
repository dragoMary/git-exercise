
#TASK 1
#Create two simple functions isOdd and isEven that each take a single Integer and return a Boolean indicating whether the passed value is odd or is even.

##An integer is even if it can be divided by 2 to produce another integer value. It is odd when dividing it by two produces a decimal value.

#Then use those functions with these test cases:
#print(isOdd(1), isEven(1))
#print(isOdd(657842), isEven(657842))
#print(isOdd(0), isEven(0))
'''
def isOdd(num):
    return num % 2 != 0

def isEven(num):
    return num % 2 == 0
print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))
'''

#Task 2:
#Create a single function getParity that does the same thing as the two functions in the previous task. This new function will accept a new positional argument of type String that will contain the type of parity we want to get (either odd or even).

#If the argument parity is different than odd and even then it should output a string message Parity indicated is unknown.

#Then design your own test cases to replicate the ones in the previous task but using the new function. Add also the following test case at the end:

#print(getParity(-2, 'number'))

'''
def getParity(num, parity):
    if parity == 'odd':
        return num % 2 != 0
    elif parity == 'even':
        return num % 2 == 0
    else:
        return 'Parity indicated is unknown.'
print(getParity(-2, 'number'))
print(getParity(1, 'odd'), getParity(1, 'even'))
print(getParity(657842, 'odd'), getParity(657842, 'even'))
print(getParity(0, 'odd'), getParity(0, 'even'))

'''

#TASK 3
#Create a single function greet that greets a person differently depending on the time of the day.
'''
from datetime import datetime

def greet(name, date:datetime):
    time = date.time()
    if time < datetime.strptime('12:00:00', '%X').time():  # X used to format the time
        return f'Good Morning, {name}!'
    else:
        return f'Good Afternoon, {name}!'


print(greet(name='John',date=datetime( 2021, 5, 7, 11, 59, 59)))
print(greet(name='John',date=datetime( 2021, 5, 7, 12, 0, 1)))

'''

#Task 4
#function should return the sum of all numbers in any of those lists and it must accept any number of parameters (use packing).

'''
def sumAll(*our_list):

    e = []             # empty list
    for i in our_list:
        s = sum(i)
        e.append(s)       # add the other list

    return sum(e)

test1 = [[0, 2, 4, 5]]
test2 = [[0, 2, 4, 5],[6],[0, 2, 4, 5, 1, 4, 3, 2]]
print(sumAll(*test1))
print(sumAll(*test2))

'''


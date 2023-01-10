'''
x = 5
y = 8
if(x == y) or (y != x):
    print('they are not equal')
else:
    print('they are equal')

  '''

'''                 #Comparisons
number = 1
while number < 1:
    print(number)
    number +=1
number1= input('enter first number ')
number2 = input('enter second number')
if int(number1) > 10 and int(number2) < 100:
    print('numbers are not equal')
if not(int(number1) > 100 and int(number2) < 10):
    print('the second number is greater than first number')
if int(number) >=100:
    print('second number is greater than or equal to first number')
if not(int(number1) < 10 and int(number2) < 100):
    print('both numbers are big!')
if int(number1) > 10 or int(number2) >=100:
    print('big numbers is set to True')
    


number = 1
while number < 1:
    print(number)
    number +=1

number3= input('enter first number ')
number4 = input('enter second number')

if int(number3) != int(number4):
    print('numbers are not equal')
if int(number4) > int(number3):
    print('second number is greater than first number')
else:
    print('second number is greater than or equal to first number')
if int(number4) >= int(number3):
    print('second number is greater than or equal to first number')
else:
    print('both numbers are not big')
if int(number3) < int(number4):
    print('number1 is smaller than number2')
else:
    print('big numbers is set to False')

'''
'''                                 #Task2
import calendar
m = calendar.month_name[1:]
print(m)

month_name = input('enter the name of th emonth: ')
if month_name == 'February':
    print('nr. of days: 28/29 days')
elif month_name in ('april', 'june', 'november'):
    print('nr. of days: 30 days')
else:
    print('wrong month name')


'''

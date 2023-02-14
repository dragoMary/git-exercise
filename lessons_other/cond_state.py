
#TASK1 - calc sum
'''
num1 = int (input('Enter first number: '))
num2 = int (input('Enter second number: '))
num3 = int (input('Enter third number: '))
a = (num1, num2, num3)
sum = sum(a)
if int(num1) == int(num2) and int(num2) == int(num3):
    print('the triple sum is', sum * 3)
else:
    print('sum is', sum )

    '''


#Task1 - Math operator

#Addition (+)
3 + 5 returns 8
3.5 + 2.7 returns 6.2
3 + 5j returns a complex number: (3+5j)
True + False returns 1
#Subtraction (-)
5 - 3 returns 2
10.5 - 4.2 returns 6.3
4 - 2j returns a complex number: (4-2j)
True - False returns 1
#Multiplication (*)
3 * 5 returns 15
3.5 * 2.5 returns 8.75
3 * 5j returns a complex number: (-15+0j)
True * False returns 0
#Division (/)
10 / 5 returns 2.0
9.0 / 3.5 returns 2.571428571428571
3 / 5j returns a complex number: (-0.6+0.2j)
True / False returns a ZeroDivisionError, since you cannot divide by zero
#Modulus (%)
10 % 3 returns 1
10.5 % 3.5 returns 2.0
10 % 5j returns a complex number: (1+1.5j)
True % False returns a TypeError, since modulus is not supported for boolean values
#Exponent (**)
2 ** 3 returns 8
3.5 ** 2.5 returns 22.64857685009486
2 ** 1j returns a complex number: (-1.1313708498984762-1.414213562373095j)
True ** False returns 1
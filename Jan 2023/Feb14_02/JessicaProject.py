

# Group Project:
# Write a program that takes two inputs (a and b), and an operator they want to perform. Your program should evaluate the resulting logical expression and return the correct boolean expression. Your program should be able to evaluate all the operators learned in today's class.

#NAND
a = input('enter the first input:')
b = input('enter the second input:')
choose = input('type an operation: NAND, XNOR, XOR, AND, NOR').upper()

if choose == 'NAND':
    if a == 1 and b == 1:
        print('the output is:', 0)
        print('result is:', 'False')
    else:
        print('the output is:', 1)
        print('the output is:', 'True')
elif choose == 'NOR':

#NOR
# a = input('enter the first input:')
# b = input('enter the second input:')


    if a == 0 and b == 0:
        print('the output is:', 1)
        print('result is:', 'True')
    else:
        print('the output is:', 0)
        print('the output is:', 'False')

elif choose == 'XOR':


 #XOR

    total = a + b
    if total == 1:
        print('the output is:', 0)
        print('result is:', 'False')

    else:
        print('the output is:', 1)
        print('the output is:', 'True')
elif choose == 'XNOR':

# XNOR # Output is true, when both inputs are the same
# A   B   O/P
# 0   0   1
# 0   1   0
# 1   0   0
# 1   1   1


    total = a + b
    if total == 1:

            print('The output is:', 0)
            print('The output is:', 'False')
    else:
            print('The output is:', 1)
            print('The output is:', 'True')

else:
    print('This is an invalid input')

#task1

'''
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)


countdown(5)
'''

#task2

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(10))

'''

#task3

def harmonic_sum(n):
    return sum([1/i for i in range(1,n+1)])


print(harmonic_sum(7))
print(harmonic_sum(4))

# is the harmonic sum of the first 5 natural numbers:
# 1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283333333333333



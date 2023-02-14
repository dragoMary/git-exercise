my_var = lambda x: x + 1

def my_ldef(x):
    return x + 1


#print(my_var(10))

def my_printer(text):
    return lambda x: f'{text}, {x}'
result = my_printer('hello')    # lambda x: f'hello, {x}'
print(result('Julia'))
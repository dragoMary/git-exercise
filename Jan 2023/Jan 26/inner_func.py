
def my_func(main_par):
    return main_par

result = my_func
print(result('any string'))

def simple_def(a, b):
    print('here is simple func')
    return a + b

def other_simp_func(func, args):
    print('here is main func')
    return func(*args)
result = other_simp_func(simple_def, [2, 3])
print(result)


def my_print(text):
    def printer():
        print(text)
    return printer()
my_print('some string to print out')
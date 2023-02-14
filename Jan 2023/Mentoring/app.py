# -recurse
# calling function inside function(itself)
#
# ==> factorial? fibonacci
#
# at the of the month, chatge teh customer credit card
# processing emails -->
#
# definition factorial
# n! = n * (n - 1)! if n = 0, return 1.
#
# 4! => 4 x (4-1)!
# 4 X 3 X (3-1)!


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))

#
# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     if m > 0 and n == 0:
#         return ackermann(m-1, 1)
#     if m > 0 and n > 0:
#         return ackermann(m-1, ackermann(m, n -1))
#     print(ackermann(4, 3))


# design a function that transfers bits that represent a
# netflix movie from point A to point B.

def transfer(list_a, list_b):
    # what is the base case?
    # if the list_a is empty, return list_b
    if not list_a:
        return list_b
    list_b.append(list_a.pop(0))
    # recurse - call the function
    return transfer(list_a, list_b)


list_a = [1, 2, 3]
list_b = []
print(list_a, list_b, 'BEFORE!!')
transfer(list_a, list_b)
print(list_a, list_b, 'After!!')


'''
def transfer_dictionaries(dict_a, dict_b):
    # forget to recurse - call the function
    # what is our base case?
    if not dict_a:  # len(dict_a) == 0:
        return dict_b
    keys = dict_a.keys()
    if len(keys) > 0:
        key = list(keys)[0]
        dict_b[key] = dict_a.pop(key)
        #dict_b[key] = dict_a[key]
        #del dict_a[key]
    return transfer_dictionaries(dict_a, dict_b)


dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {}
transfer_dictionaries(dict_a, dict_b)
print(dict_a, dict_b)


'''



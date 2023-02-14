import re
def is_math_expression(string):
    result = r'^[\d\s+\-*/%()]+$'
    return bool(re.match(result, string))
print(is_math_expression("5 + 2"))

def is_math_expression(string):
    result = r'^[\d\s+\-*/%()]+$'
    return bool(re.match(result, string))
print(is_math_expression("9 * 1"))


def is_math_expression(string):
    result = r'^[\d\s+\-*/%()]+$'
    return bool(re.match(result, string))
print(is_math_expression("hello world"))


def is_math_expression(string):
    result = r'^[\d\s+\-*/%()]+$'
    return bool(re.match(result, string))
print(is_math_expression("123" ))


def is_math_expression(string):
    result = r'^[\d\s+\-*/%()]+$'
    return bool(re.match(result, string))
print(is_math_expression("5 + foo" ))

import re
str = '0023.07623070'
str = re.sub(r'^00', '', str)
print (str)

text = 'hello world'
result = re.search(r'hello world', text)
print(result)

str = '01230'
str = re.sub(r'^0*', '', str)
print (str)


str = '01230'
str = re.sub(r'0*$', '', str)
print (str)

str = '01230'
str = re.sub(r'123', '', str)
print (str)


str = '01230'
str = re.sub(r'^0*|0*$', '', str)
print (str)

import re

def make_happy(sentence):
    return re.sub(':\\(', ':)', sentence)
print(make_happy("My current mood: :("))


def make_happy(sentence):
    return re.sub('\\(', ')', sentence)
print(make_happy("print('x(')"))




def make_happy(sentence):
    return re.sub(':\\(', ':)', sentence)
print(make_happy("I was hungry 8)"))



str = 'I am feeling :) but now :( '
str = re.sub(r':[-]\)',':-(',str)
print(str)





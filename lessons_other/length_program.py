
'''
x = "hello world"
if (len(x)) % 2 == 0:
        print('"hello world "   -->    "even"')
else:
        print('"hello world"    -->    "odd"')



y= "hello planet"
if (len(y)) % 2 == 0:
        print('"hello planet "   -->    "even"')
else:
        print('"hello planet"    -->    "odd"')

'''


#variation on the same theme

words = ('planet', 'world', 'fo', 'bar', 'baz', 'qux')
#even_length_words = [word for word in words if len(word) % 2 == 1]
#print(even_length_words)
for word in words:
    if len(word) % 2 == 1:
        print( word)
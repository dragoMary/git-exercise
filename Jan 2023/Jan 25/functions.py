
#def hello(name):
   # print('how are you')
    #a = 50
   # return a
    #return f'hello {name}!'
#print(hello('James how are you today?'))

#greet = hello('James')
#print(greet)


#def addition(a, b):
    #return a + b
#print(addition(100, 60))

#def addition(a=200, b=300):  # it will show the last values i gave: 100, 50
    #return a + b
#print(addition(100, 50))


#def addition(a=200, b=300, c=400, d=600):
    #return a + b + c + d
#print(addition(c=4000))

#def addition(a=200, b=300, c=400, d=600):
    #return a + b + c + d
#num1 = 700000
#print(addition(num1))


def addition (*args):
    return args[2] + args[3]
num = [ 800, 200, 300, 500]
print(addition(*num))
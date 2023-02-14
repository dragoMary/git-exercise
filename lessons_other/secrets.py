

secret = input('enter your secret:')
if len(secret) > 8 :
    print(secret)
else:
    print('The secret must be at least 8 characters')
    secret = input('secret:')
love_name = input('enter your love name:')

year = input('enter your year of birth:')
print( love_name +  year + secret [::-1])


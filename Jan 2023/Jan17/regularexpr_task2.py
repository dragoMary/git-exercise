

#(\W|^)[\w.-]{0,25}@(gmail|deliveryhero).com(\W|$)
#--> emails with TLD gmail.com or deliveryhero.com

import re
#Task 1
text = 'i want a red color or a blue colour'
result =re.findall('red color|blue colou?r', text)
print(result)



#TASK 2
text = 'dragomir@gmail.com'
text2 = 'dragomir@deliveryhero.com'
result = re.search ('(\W|^)[\w.-]{0,25}@(gmail|deliveryhero).com(\W|$)',text)
result2 = re.search ('(\W|^)[\w.-]{0,25}@(gmail|deliveryhero).com(\W|$)',text2)
print(result)
print(result2)


#TASK 3
#^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$

text = ' drg* .3D'
result = re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}$', text)
print(result)

#Task 4
text = '#f0f'
result = re.search('^#?([a-f0-9]{6}|[a-f0-9]{3})$', text)
print(result)
#match any hex color code, whether it starts with "#" or not, and whether it is a 6-digit or 3-digit code.


#TASK 5
text = 'workdone'
result = re.search('done$', text)
print(result)
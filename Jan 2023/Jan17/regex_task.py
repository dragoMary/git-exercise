
import re

#TASK 1
text = 'Berlin is a world city of culture, politics, media and science.'
result = re.search(r'\s', text)
print(result)

#TASK 2

#text = 'Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburgs capital.'
#result = re.search('Frankfurt', text)
#print(result)

#TASK 3
#text = 'Berlin is a city of culture.'
#result = re.sub(r"\s", "-", text)
#print(result)


#TASK 4

#text = 'Berlin is a city of culture.'
#result = re.search(r"in", text)
#print(result)

#TASK 5

#text = 'Berlin is a city of culture.'
#result = re.search(r"\bB\w+", text)
#print(result.start())
#print(result.end())

#Task6

#text = 'The rain in Spain.'
#result = len(re.findall('ai', text))
#print(result)
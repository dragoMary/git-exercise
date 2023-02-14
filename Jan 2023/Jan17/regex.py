import re

#rain =  "The rain was falling heavily. It was like driving through a thick curtain of water. He eased off the accelerator a little. Had to be careful driving on wild nights like these.The last thing you’d want is to have an accident or breakdown. You just want to be at home on these stormy nights. The thwack-thwack of the"
#numbers ='39801 356, 2102 1111'
#result = re.search('\d{3} \d{3}', numbers)
#result = re.split('\s', rain)
#result = re.split('like', rain)
#result = re.sub('[t,T]he', 'AAA', rain, 3)
#print(len(re.findall('AAAA', result)))
#result = re.findall('water', rain)

#print(result)
#print(result.start())
#print(result.end())
#print(len(result))
#print(result.span())


#sentence = 'Berlin is a beautiful city'
#result = re.search('\\bBerlin', sentence)   #poti folosi si r' ca raw format, plasat la inceput in inter parantezei
#result = re.search(r'\bc\w+', sentence) #boundary works also if you look for more letters using w+
numbers ='3983 014 356, 2102 1111'
result = re.search('\d{3}\s\d{3}', numbers)
print(result)
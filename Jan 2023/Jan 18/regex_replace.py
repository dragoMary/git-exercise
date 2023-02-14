

import re

#quote = 'If you hear a voice within you say, ‘You cannot tttpaint#,’ then by all means paint, and that voice will be silenced.'
#result = re.sub('tt(\w+)#', r'\1', quote)   # \1 se refera la 1 group si anume la grupul (\w+)
#result = re.sub('t+(\w+)(#)', r'\2', quote)
#print(quote)
#result = re.sub('p\w+', 'swim', quote)

text = 'good morning'

result = re.match('good', text)

result = re.match('g\w+', text)  # return 'good' as well with this syntax

print(result)



#def digit_filter(strings):
    #index = 0
    #while index < len(strings):
        #if any(char.isdigit() for char in strings[index]):
            #strings.pop(index)
        #else:
            #index += 1
    #return strings

l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
#print(digit_filter(l33t))



#if current str has digit then is removed with pop
#if str dont have digit, index is incremented and the loop goes on until the last str.

for i in l33t:                          # second version
    for j in i:
        if j.isdigit():
            l33t.remove(i)
            break
print(l33t)
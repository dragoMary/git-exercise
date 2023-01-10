import sys
import getopt

file_name = sys.argv[0]
other_data = sys.argv[1:]

x, y = getopt.getopt(other_data, 'hm:', ['help', 'message=', 'name='])      #store rec data and not rec data


print(x)   #rec_data
print(y)   #not_rec_data

name = None

for item in rec_data:
    print(item)


    if item[0] == '-h' or item[0] == '--help':
        print('some message')

    elif item[0] == '-m' or item[0] == '--message':
        print('message is', item[1])

    elif item[0] =='--name':
        name = item[1]

if name:
    print('hello', name)
else:
    print('hello user')
'''
import getopt
import sys
name = None

options, args = getopt.getopt(sys_argv[1:], 'hm:', ['help', 'name='])
print(options, args)

for options, in options:
    print(options)
    if options[0] in ('-h', '--help'):
        print('this is: -n <name>')
        sys.exit()
    elif options[0] in ('-n', '--name'):
        name=options[1]
        print('Good Morning {name}! ')
    if name:
        print('Good Morning {name}! ')
    else:
        print('hello folks')

'''


import getopt
import sys

name = None

opts, args = getopt.getopt(sys.argv[1:], "hn:", ["help", "name="])

for opt in opts:
    if opt[0]in ('-h', '--help'):
        print('you can type anything here')

    elif opt[0] in ('-n', '--name'):
        name=opt[1]
        print(f'Good Morning {name}!')
if name:
        print(f'Good Morning {name}!')
else:
    print('Hello folks')
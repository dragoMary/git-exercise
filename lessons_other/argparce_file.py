import argparse
import sys
parser = argparse.ArgumentParser()

parser.add_argument(
    '-f',
    '--first_name',
    metavar='First name' ,

    type=string,
    nargs='?',
    help='Your first name',
    default='user'
)

 parser.add_argument(

     'a',
     '--age',
     metavar='Age',
     type=int,
     narge='?',
     help='enter your age'
 )


run = parser.parse_args()
print('Hello', run.first_name)
if run.age:
    print('you are', run.age, 'years old')
else:
    print('age is not specified')
import sys

options = sys.argv[1:]

if '--help' in options:
    print('This is a small help text')
elif '--fast' in options:
    print('fast mode enabled')
else:
    print('slow mode enabled')
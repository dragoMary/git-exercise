import argparse


parser = argparse.ArgumentParser(prog='app3.py')


parser.add_argument('--first_name', nargs='?', default='Larry')
parser.add_argument('--last_name', nargs='?', default='Hanson')
parser.add_argument('--age', nargs='?', default=100, type=int)


parser.add_argument('--fast')


args = parser.parse_args()


if args.fast:
    print("fast mode enabled")

print(f"Hello {args.first_name} {args.last_name}! I see that you have had {args.age + 1} birthdays.")
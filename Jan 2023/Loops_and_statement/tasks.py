#task1
'''

num = int(input("Enter a number: "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

'''

#task2
'''
for i in range(1, 10):
    for j in range(i):
        print(i, end='')
    print('')

'''
#task3
'''
word = input("Enter a word: ")

reversed_word = ""
for i in range(-1, -len(word) - 1, -1):
    reversed_word += word[i]

print("The reversed word is:", reversed_word)

'''
#task4
'''
text = "Hello, I love you, won't you tell me your name?"

new_text = ""
for char in text:
    if char == 'o':
        new_text += 'O'
    else:
        new_text += char

print(new_text)

'''


#task5

text = input("Enter your characters: ")

num_digits = 0
num_letters = 0
for char in text:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1

print("Number of digits:", num_digits)
print("Number of letters:", num_letters)

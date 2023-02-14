'''
i = -5
while i <= 5:
    if i == 0:
        i += 1
    else:
        print(i)
        i += 1


string = 'Sie sind dabei an diesem Samstag und am kommenden Montag auch.'
new_string = ''
index = 0


while index < len(string):
    char = string[index]
    if char.islower():
        new_string += char.upper()
    elif char.isupper():
        new_string += char.lower()
    else:
        new_string += char
    index += 1

print(new_string)

'''

'''
counter = 0
total = 0
while counter < 3:
    number = int(input("Enter a number: "))
    if number == 0:
        print("Invalid input. Number cannot be 0.")
        continue
    counter += 1
    total += number
average = total / counter
print("The average of the numbers is: ", average)

'''

'''
text = "She came to me one morning One lonely Sunday morning Her long hair flowing in the mid-winter wind I know not how she found me For in darkness I was walking And destruction lay around me from a fight I could not win"

letter = input('What letter should be found?:')

index = 0
while index < len(text):
    if text[index] == letter:
        print("letter", letter, "found at index", ":", [index])
    index += 1
    
    '''

counter = 0
while True:
    a = int(input("Type starting integer: "))
    b = int(input("Type ending integer: "))
    c = int(input("Type divisor: "))
    if c == 0:
        break
    divisible_numbers = 0
    for i in range(a, b+1):
        if i % c == 0:
            divisible_numbers += 1
            print(i, end=", ")
    print("Between", a, "and", b, "there are", divisible_numbers, "numbers divisible by", c)
print("Program finished")




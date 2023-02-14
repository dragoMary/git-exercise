


word = 'doom'
a = input('inatorInator("Doom")')
def inatorInator(word):
    if word[-1].isalpha() and word[-1].isupper():
        word = word.lower()
    if word[-1] in 'aeiouAEIOU':
        word += '-inator'
    else:
        word += 'inator'
    word += str(len(word)-6) + '000'
    return word
print(inatorInator(word))


word = 'Shrink'
a = input('inatorInator("Shrink")')
def inatorInator(word):
    if word[-1].isalpha() and word[-1].isupper():
        word = word.lower()
    if word[-1] in 'aeiouAEIOU':
        word += '-inator'
    else:
        word += 'inator'
    word += str(len(word)-6) + '000'
    return word
print(inatorInator(word))


word = 'EvilClone'
a = input('inatorInator("EvilClone")')
def inatorInator(word):
    if word[-1].isalpha() and word[-1].isupper():
        word = word.lower()
    if word[-1] in 'aeiouAEIOU':
        word += '-inator'
    else:
        word += 'inator'
    word += str(len(word)-7) + '000'
    return word
print(inatorInator(word))

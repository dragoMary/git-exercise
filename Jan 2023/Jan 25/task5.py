def pig_latin(strings, suffix='ay', single=False):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = strings.split()
    latin_words = []
    for word in words:
        if word[0].lower() in vowels:
            latin_word = word + suffix
        else:
            latin_word = word[1:] + word[0] + suffix.capitalize() # with that we remove the first char of original word
        latin_words.append(latin_word)
    if single is True:
        return ' '.join(latin_words)      # with join return the string of our list
    else:
        return latin_words






test1_data = "Word Apple"
test1_config = {}

test2_data = "Python Functions"
test2_config = {"suffix": "oy"}

test3_data = "If the word starts with a vowel add the suffix to the word"
test3_config= {"single": True, "suffix": "ep"}

print(pig_latin(test1_data, *test1_config))
print(pig_latin(test2_data, **test2_config))
print(pig_latin(test3_data, **test3_config))







s1 = 'CAPS LOCK DAY IS OVER'
s2 = 'toDay is Not caps Lock day.'
s3 = 'Let us stay calm, no need to panic.'
sn = (s1, s2, s3)
for s in sn:
    def normalize(s):
        if s.isupper():
            first_letter = s[0]
            rest_of_sentence = s[1:].lower()
            return first_letter + rest_of_sentence + '!'
        else:
            first_letter = s[0].upper()
            rest_of_sentence = s[1:].lower()
            return first_letter + rest_of_sentence

    print(normalize(s))

import string
sentence = input('Enter a sentence:')

sentence_len1 = 0
sentence_len2 = 0
alphabet = string.ascii_lowercase
alphabet_2 = string.ascii_uppercase

for i in sentence:
    if i in alphabet:
        sentence_len1 += 1
    elif i in alphabet_2:
        sentence_len2 += 1
print('lower:',sentence_len1, '\nupper:',sentence_len2)
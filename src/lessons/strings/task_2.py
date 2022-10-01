sentence = input('Enter a sentence:')

sentence = sentence.split()

sentence_len = 0
sentence_result = ''

for i in sentence:
    if len(i) > sentence_len:
        sentence_len = len(i)
        sentence_result = i
print(sentence_result)
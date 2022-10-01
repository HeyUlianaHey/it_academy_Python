sentence = input('Enter a sentence:')
sentence = sentence.replace(' ', '')

result = ''

for i in sentence:
    if i not in result:
        result += i
print(result)

# for i in range(len(sentence)):
#     if result.find(sentence[i]) == -1 and sentence[i] != ' ':
#         result += sentence[i]
# print(result)
command_names = ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10", "K11", "K12", "K13", "K14", "K15", "K16"]
match_1 = [3,1,2,4,5,3,1,4,2,3,1,1,2,3,4,1]
match_2 = [2,1,1,3,1,3,2,4,4,1,3,1,3,2,3,1]
pair1 = command_names[:8]
pair2 = command_names[15:7:-1]       # в обратном порядке

ochki1 = match_1[:8]
ochki2 = match_1[15:7:-1]          #очки матч 1

ochki11 = match_2[:8]
ochki22 = match_2[15:7:-1]          #очки матч 2

result_1m = []
result_2m = []   #Результат матчей 1 и 2
inside1 = []
inside2 = []
result_1m_2m_number = []
result_1m_2m_letter = []

inside1_3 = []
inside2_3 = []
result_3m_number = []            #Результат матча 3
result_3m_letter = []

inside1_4 = []
inside2_4 = []
result_4m_number = []            #Результат матча 4
result_4m_letter = []

# 1е условие
for pair_1, pair_2 in zip(pair1, pair2):
    a = pair_1, pair_2
    print(f"{pair_1}:{pair_2}", end=" ")
print()
print("Матч_1:")
for ochki_1, ochki_2 in zip(ochki1, ochki2):
    print(f"{ochki_1}:{ochki_2}", end=" ")
print()
print("Матч_2:")
for ochki_11, ochki_22 in zip(ochki11, ochki22):
    print(f"{ochki_11}:{ochki_22}", end=" ")
print()
for r1, r2 in zip(ochki1,ochki11):
    result_1m.append(r1+r2)

for r1, r2 in zip(ochki2,ochki22):
    result_2m.append(r1+r2)

print("Результат матчей 1 и 2:")
for res1, res2 in zip(result_1m, result_2m):
    print(f"{res1}:{res2}", end=" ")
    inside1.append(res1)
    inside2.append(res2)
    if res1 > res2:
        result_1m_2m_number.append(res1)
    else:
        result_1m_2m_number.append(res2)
print()
for i in range(8):
    if inside1[i] > inside2[i]:
        result_1m_2m_letter.append(pair1[i])
    elif inside2[i] > inside1[i]:
        result_1m_2m_letter.append(pair2[i])
print(result_1m_2m_letter)
print(result_1m_2m_number)

ochki1_3 = result_1m_2m_number[:4]         #очки матч 3
ochki2_3 = result_1m_2m_number[7:3:-1]
letter1_3 = result_1m_2m_letter[:4]         #буквы матч 3
letter2_3 = result_1m_2m_letter[7:3:-1]
print("Результат матча 3:")
for res1, res2 in zip(ochki1_3, ochki2_3):
    print(f"{res1}:{res2}", end=" ")
    inside1_3.append(res1)
    inside2_3.append(res2)
    if res1 > res2:
        result_3m_number.append(res1)
    else:
        result_3m_number.append(res2)
print()
for i in range(4):
    if inside1_3[i] > inside2_3[i]:
        result_3m_letter.append(letter1_3[i])
    elif inside2_3[i] > inside1_3[i]:
        result_3m_letter.append(letter2_3[i])
print(result_3m_number)
print(result_3m_letter)

ochki1_4 = result_3m_number[:2]         #очки матч 4
ochki2_4 = result_3m_number[3:1:-1]
letter1_4 = result_3m_letter[:2]         #буквы матч 4
letter2_4 = result_3m_letter[3:1:-1]
print("Результат матча 4:")
for res1, res2 in zip(ochki1_4, ochki2_4):
    print(f"{res1}:{res2}", end=" ")
    inside1_4.append(res1)
    inside2_4.append(res2)
    if res1 > res2:
        result_4m_number.append(res1)
    else:
        result_4m_number.append(res2)
print()
for i in range(2):
    if inside1_4[i] > inside2_4[i]:
        result_4m_letter.append(letter1_4[i])
    elif inside2_4[i] > inside1_4[i]:
        result_4m_letter.append(letter2_4[i])
print(result_4m_number)
print(result_4m_letter)
#очки матч Finish
if result_4m_number[0] > result_4m_number[1]:
    print("Команда победитель :", result_4m_letter[0])
else:
    print("Команда победитель :", result_4m_letter[1])
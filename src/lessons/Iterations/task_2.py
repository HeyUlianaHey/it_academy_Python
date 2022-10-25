import csv

csvfile = csv.DictReader(open('library.csv', newline=''), delimiter=' ', quotechar='|', fieldnames=["AVTOR", "NAME",
                                                                                                   "YEAR", "TOPIC"])  # открываем csv файл
enter = input('Введите фамилию автора и доп параметр:')
enter = enter.split()
d = {}
d["AVTOR"] = enter[0]
d["YEAR"] = enter[1]

search = []
l = []

for row in csvfile:
    if d.get('AVTOR') in row.get("AVTOR") and d.get("YEAR") == row.get("YEAR"):
        search.append(row.get('TOPIC'))
        print(row.get('TOPIC'))

    elif d.get('AVTOR') in row.get("AVTOR") and (d.get("YEAR") == "First" or d.get("YEAR") == "Last"):
        out = row.get('NAME')
        l.append(out)
        search.append(out)

if d.get("YEAR") == "First":
    print(l[0])
elif d.get("YEAR") == "Last":
    print(l[-1])

if search == []:
    print("not Found")
else:
    print("Found")
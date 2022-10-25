import csv

topicc = set(input('Введите список тем через запятую:').split(','))
number = (input('Введите число:'))

value = ''
books = []
with open('library.csv') as f:
    for d in csv.DictReader(f, delimiter=' ', quotechar='|', fieldnames=["AVTOR", "NAME","YEAR", "topic"]):
        value = d.get('topic')
        value = str(value)
        topic = set(value.split(','))
        match = topic & topicc
        if match:
            d["match"] = len(match)
            books.append(d)

result = sorted(books, key=lambda d: d["match"], reverse=True)
if number == '':
    for i in result:
        print(i)
else:
    for i in result[:int(number)]:
        print(i)
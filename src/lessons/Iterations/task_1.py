skobka = input("write sentence with brackets:")

skobki_open = ('(', '[', '{')
skobki_close = (')', ']', '}')
inside = []  #([{

for i in skobka:               #([{ correct }])
    if i in skobki_open:
        inside.append(i)
    if i in skobki_close:
        if len(inside) == 0: #нет open скобок
            print('неверно')
        index = skobki_close.index(i) #ищем индекс close скобок  /2-индекс/ (')', ']', '}')
        # print(index)
        open_skobki = skobki_open[index] #передаем сюда индекс 2 == {
        # print(open_skobki) #выведет нам элеменет - {
        if inside[-1] == open_skobki:   #inside[-1]=={
            inside = inside[:-1] #([
        else:
            print('неверно')
if inside == []:
    print('верно')
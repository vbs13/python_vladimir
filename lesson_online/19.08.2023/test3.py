a = input()
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

for i in a:
    print(alf[(alf.index(i) + 3) % len(alf)], end='')
s = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
res = ''

alf_rus = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя']

for i in len(s):
    res += alf_rus[s[i]]
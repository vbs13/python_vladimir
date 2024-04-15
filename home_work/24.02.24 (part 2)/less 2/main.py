n = input('Введите строку: ')
x = n.split(' ')
print(x)
m = 0
s = ''

for i in x:
    if len(i) > m:
        m = len(i)
        s = i
    if len(i) == m:
        s = s
        m = m

print('Самое длинное слово:', s)
print('Длина этого слова:', m)
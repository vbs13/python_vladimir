n = int(input('Количество карт: '))
summ = 0
summ1 = 0

for i in range(1, n):
    a = int(input('Введите карту: '))
    summ += a

for i in range(1, n + 1):
    summ1 += i

print('Пропавшая карта: ', summ1 - summ)
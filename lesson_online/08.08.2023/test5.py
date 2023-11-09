grant = int(input())
expens = int(input())
summ = 0
summ1 = 0

for i in range(1, 11):
    summ = expens - grant + summ1
    print(i, 'месяц траты:', round(expens, 1), 'не хватает', round(summ, 1))
    expens *= 1.03
    summ1 = summ

print(round(summ, 1))
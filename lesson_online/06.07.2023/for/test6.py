n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
summ = 0

for n in range(n1, n2 + 1):
    summ += n

print(summ)

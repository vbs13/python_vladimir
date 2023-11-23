def nod(a, b):
    x = min(a, b)
    y = max(a, b)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
print('Наибольший общий делитель:', nod(num1, num2))
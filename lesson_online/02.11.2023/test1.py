plus = 0
minus = 0

while True:
    a = int(input('Введите число: '))
    if a > 0:
        plus += 1
    elif a < 0:
        minus += 1
    else:
        break


print(plus, minus)
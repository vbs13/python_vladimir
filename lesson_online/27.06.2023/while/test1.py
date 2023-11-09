pas = '1465'
p = input('Введите код: ')
tryy = 0

while p != pas:
    print('Неверно')
    p = input('Введите код: ')
    tryy += 1

print('Верно', tryy)
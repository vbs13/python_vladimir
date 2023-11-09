a = int(input('Строка: '))
b = int(input('Столбец: '))

for i in range(a):
    for j in range(b):
        if i == 0:
            print('-', end='')
        elif j == 0 or j == b - 1:
            print('|', end='')
        else:
            print(' ', end='')
    print()
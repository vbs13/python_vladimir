a = int(input('Введите размер матрицы: '))

for i in range(a):
    for j in range(a):
        if i ==  a // 2 or j == a // 2:
            print('0', end=' ')
        elif i == 0 or i == a - 1 or j == 0 or j == a - 1:
            print(1, end=' ')
        else:
            print('*', end=' ')
    print()

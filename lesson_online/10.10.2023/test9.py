n = 9

for j in range(n):
    for i in range(n):
        if (j == 0) or (j == n - 1):
            print('-', end=' ')
        elif i == j and i == n // 2:
            print('X', end=' ')
        elif i == 0 or i == n - 1:
            print('|', end=' ')
        elif i == j:
            print('\\', end=' ')
        elif i + j == n - 1:
            print('/', end=' ')
        else:
            print('*', end=' ')
    print()
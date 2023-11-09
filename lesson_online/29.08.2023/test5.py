for i in range(20):
    for j in range(50):
        if i == 10:
            print('-', end='')
        elif j == 24:
            print('|', end='')
        elif i + j == 19:
            print('/', end='')
        elif i == j - 29:
            print('\\', end='')
        else:
            print(' ', end='')
    print()
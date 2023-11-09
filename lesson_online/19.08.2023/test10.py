for i in range(20):
    for j in range(50):
        if i == 10 and j == 25:
            print('+', end='')
        elif i == 10:
            print('-', end='')
        elif j == 25:
            print('|', end='')
        else:
            print(' ', end='')
    print()
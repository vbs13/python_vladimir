n = int(input())

for i in range(n + 1):
    for j in range(n + 1):
        if i + j > n:
            print(' ', end=' ')
        else:
            print(j + i, end=' ')
    print()
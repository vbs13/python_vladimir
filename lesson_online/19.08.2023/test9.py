a = int(input('Размер матрицы: '))

for i in range(1, a + 1):
    for j in range(1, a + 1):
        if j % 3 == 0:
            print(j, end='\t')
        else:
            print(i, end='\t')
    print()
    
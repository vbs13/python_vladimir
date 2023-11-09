def plusi(x, y: int):
    for j in range(y):
        for i in range(x):
            print(j + i, end='\t')
        print()


def umnoj(x, y: int):
    for j in range(1, y + 1):
        for i in range(1, x + 1):
            print(j * i, end='\t')
        print()


plusi(5, 3)
print()
umnoj(5, 3)
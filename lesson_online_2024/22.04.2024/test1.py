mas = [[1, 2, 2], [3, 4, 8], [7, 9, 10], [11, 54, 0], [13, 4, 4]]
mas1 = {}
k = 0

for i in range(len(mas)):
    if int(mas[i][0] % 2 == 0) + int(mas[i][1] % 2 == 0) + int(mas[i][2] % 2 == 0) == 2:
        if len(set(mas[i])) == 3:
            if max(mas[i]) < (mas[i][0] + mas[i][1] + mas[i][2]) - max(mas[i]):
                k += 1
                print(mas[i])
print(k)
mas = [30, 4, 5, 7, 9]
n = 0
maxx = 0
for i in range(len(mas) - 1):
    if mas[i] % 2 != 0 and mas[i + 1] % 2 != 0:
        n += 1
        if mas[i] + mas[i + 1] > maxx:
            maxx = mas[i] + mas[i + 1]
print(n, maxx)
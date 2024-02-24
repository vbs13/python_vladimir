mas = [int(x) for x in open('17_13088.txt')]
r = max([x for x in mas if x % 100 == 17])

res = []
for i in range(len(mas) - 2):
    if (int(mas[i] in range(1000, 10000)) + int(mas[i + 1] in range(1000, 10000)) + int(mas[i + 2] in range(1000, 10000))) == 2:
        if int(mas[i] % 5 == 0) + int(mas[i + 1] % 5 == 0) + int(mas[i + 2] % 5 == 0) >= 1:
            if (mas[i] + mas[i + 1] + mas[i + 2]) > r:
                res.append(mas[i] + mas[i + 1] + mas[i + 2])

print(len(res), max(res))


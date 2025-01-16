mas = [int(x) for x in open('17_19249.txt')]
maxx = max([x for x in mas if abs(x) % 100 == 43 and abs(x) in range(10000, 100000)])
res = []

for i in range(len(mas) - 2):
    if (abs(mas[i]) % 100 == 43 and abs(mas[i]) in range(10000, 100000)) \
            or (abs(mas[i + 1]) % 100 == 43 and abs(mas[i + 1]) in range(10000, 100000)) \
            or (abs(mas[i + 2]) % 100 == 43 and abs(mas[i + 2]) in range(10000, 100000)):
        if mas[i] ** 2 + mas[i + 1] ** 2 + mas[i + 2] ** 2 <= maxx ** 2:
            res.append(mas[i] ** 2 + mas[i + 1] ** 2 + mas[i + 2] ** 2)

print(len(res), min(res))
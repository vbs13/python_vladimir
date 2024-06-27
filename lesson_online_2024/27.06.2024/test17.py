mas = [int(x) for x in open('17_17611.txt')]
mas1 = max([x for x in mas if abs(x) in range(1000, 10000) and abs(x) % 10 == 7])
res = []

for i in range(len(mas) - 2):
    if ((abs(mas[i]) in range(1000, 10000) and abs(mas[i]) % 10 == 7) \
            + (abs(mas[i + 1]) in range(1000, 10000) and abs(mas[i + 1]) % 10 == 7) \
            + (abs(mas[i + 2]) in range(1000, 10000) and abs(mas[i + 2]) % 10 == 7)) >= 2:
        if (mas[i] + mas[i + 1] + mas[i + 2]) > mas1:
            res.append(mas[i] + mas[i + 1] + mas[i + 2])
print(len(res), max(res))
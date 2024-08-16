mas = [int(x) for x in open('17_11625.txt')]
maxx = max([x for x in mas if abs(x) % 10 == 3])
res = []

for i in range(len(mas) - 2):
    if ((mas[i] % 2 == 0) + (mas[i + 1] % 2 == 0) + (mas[i + 2] % 2 == 0)) == 2:
        if (mas[i] + mas[i + 1] + mas[i + 2]) >= maxx:
            res.append(mas[i] + mas[i + 1] + mas[i + 2])
print(len(res), sum(res))
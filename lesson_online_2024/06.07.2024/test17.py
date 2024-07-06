mas = [int(x) for x in open('17_17680.txt')]
minn = min([x for x in mas if x % 41 == 0 and x > 0])
res = []

for i in range(len(mas) - 1):
    if mas[i] != mas[i + 1]:
        if (abs(mas[i] - mas[i + 1])) % minn == 0:
            res.append(mas[i] + mas[i + 1])

print(len(res), max(res))
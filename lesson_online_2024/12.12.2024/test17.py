mas = [int(x) for x in open('17 (2).txt')]
minn = min([x for x in mas if x % 2025 == 0 and x > 0])
res = []


for i in range(len(mas) - 3):
    if mas[i] > 0 and mas[i + 3] > 0:
        if abs(mas[i + 2] - mas[i + 1]) <= minn:
            res.append(mas[i] + mas[i + 1] + mas[i + 2] + mas[i + 3])
print(len(res), min(res))
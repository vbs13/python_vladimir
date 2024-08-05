mas = [int(x) for x in open('17_16328.txt')]
minn = min([x for x in mas if x % 19 == 0])
res = []

for i in range(len(mas) - 1):
    if ((mas[i] % minn) == 0) or ((mas[i + 1] % minn) == 0):
        res.append(mas[i] + mas[i + 1])

print(len(res), max(res))
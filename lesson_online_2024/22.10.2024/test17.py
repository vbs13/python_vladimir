mas = [int(x) for x in open('17_17873.txt')]
minn = min(mas)
res = []

for i in range(len(mas) - 1):
    if mas[i] % 16 == minn or mas[i + 1] % 16 == minn:
        res.append(mas[i] + mas[i + 1])

print(len(res), max(res))
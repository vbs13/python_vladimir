mas = sorted([int(i) for i in open('26 (1).txt')])[::-1]

k = [mas[0]]
for i in range(len(mas) - 1):
    if k[-1] - mas[i] >= 3:
        k.append(mas[i])

print(len(k), k[-1])
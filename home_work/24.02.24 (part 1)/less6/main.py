mas = [int(x) for x in open('17_12106.txt')]
minn = min([x for x in mas if x % 117 == 0 and x > 0])
mas1 = []

for i in range(len(mas) - 1):
    if ((mas[i] > 0) and (mas[i + 1] < 0)) or ((mas[i] < 0) and (mas[i + 1] > 0)):
        if (mas[i] + mas[i + 1]) % minn == 0:
            mas1.append((mas[i] ** 2) + (mas[i + 1] ** 2))
print(len(mas1), min(mas1))
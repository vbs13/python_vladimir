mas = [int(x) for x in open('17_17558.txt')]
mas1 = len([x for x in mas if x % 32 == 0])
mas2 = []

for i in range(len(mas) - 1):
    if (mas[i] < 0) or (mas[i + 1] < 0):
        if (mas[i] + mas[i + 1]) < mas1:
            mas2.append(mas[i] + mas[i + 1])

print(len(mas2), max(mas2))
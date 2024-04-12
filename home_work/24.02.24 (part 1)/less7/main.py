mas = [int(x) for x in open('17_9786.txt')]
maxx = max([x for x in mas if abs(x) % 100 == 25])
mas1 = []

for i in range(len(mas) - 2):
    if int(abs(mas[i]) in range(1000, 10000)) + int(abs(mas[i + 1]) in range(1000, 10000)) + int(abs(mas[i + 2]) in range(1000, 10000)) <= 2:
        if mas[i] + mas[i + 1] + mas[i + 2] <= maxx:
            mas1.append(mas[i] + mas[i + 1] + mas[i + 2])

print(len(mas1), max(mas1))
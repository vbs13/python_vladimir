mas = [int(x) for x in open('17 (2).txt')]
maxx = max([x for x in mas if abs(x) % 1000 == 121])
# print(mas)
print(maxx)
mas1 = []

for i in range(len(mas) - 2):
    # print(mas[i], mas[i + 1], mas[i + 2])
    if (int(abs(mas[i]) in range(1000, 10000) and mas[i] % 2 == 0) + int(abs(mas[i + 1]) in range(1000, 10000) and mas[i + 1] % 2 == 0) + int(abs(mas[i + 2]) in range(1000, 10000) and mas[i + 2] % 2 == 0)) <= 1:
        if mas[i] + mas[i + 1] + mas[i + 2] <= maxx:
            mas1.append(mas[i] + mas[i + 1] + mas[i + 2])

print(len(mas), max(mas))
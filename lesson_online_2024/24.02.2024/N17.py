mas = [int(x) for x in open('17_10100.txt')]
r = max([x for x in mas if x % 100 == 13])

max_sum = 0
k = 0
for i in range(len(mas) - 2):
    if int(mas[i] in range(100, 1000)) + int(mas[i + 1] in range(100, 1000)) + int(mas[i + 2] in range(100, 1000)) == 2:
        if (mas[i] + mas[i + 1] + mas[i + 2]) <= r:
            k += 1
            max_sum = max(mas[i] + mas[i + 1] + mas[i + 2], max_sum)

print(k, max_sum)

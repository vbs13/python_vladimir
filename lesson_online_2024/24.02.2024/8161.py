mas = [int(x) for x in open('17_8161.txt', 'r')]

max_3 = max([x for x in mas if x in range(100, 1000)])

res = []
for i in range(len(mas) - 1):
    if (abs(mas[i]) in range(100, 1000) and abs(mas[i + 1]) not in range(100, 1000)) or (abs(mas[i]) not in range(100, 1000) and abs(mas[i + 1]) in range(100, 1000)):
        if mas[i] + mas[i + 1] < max_3:
            res.append(mas[i] + mas[i + 1])

print(len(res), max(res))
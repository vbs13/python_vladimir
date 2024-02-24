mas = [int(x) for x in open('17_12926.txt')]
max_2 = max([x for x in mas if x in range(10, 100)])

A = -11111111111111111
for i in range(len(mas) - 3):
    if abs(mas[i]) % 10 == abs(mas[i + 1]) % 10 == abs(mas[i + 2]) % 10 == abs(mas[i + 3]) % 10:
        A = max(mas[i] + mas[i + 1] + mas[i + 2] + mas[i + 3], A)

res = []
for i in range(len(mas) - 4):
    if int(mas[i] < A) + int(mas[i + 1] < A) + int(mas[i + 2] < A) + int(mas[i + 3] < A) + int(mas[i + 4] < A) == 1:
        if (mas[i] + mas[i + 1] + mas[i + 2] + mas[i + 3] + mas[i + 4]) % max_2 == 0:
            res.append(mas[i] + mas[i + 1] + mas[i + 2] + mas[i + 3] + mas[i + 4])

print(len(res), min(res))

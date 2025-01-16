mas = sorted([list(map(int, x.split())) for x in open('107_26.txt')])

for i in range(len(mas) - 1):
    if mas[i][0] == mas[i + 1][0]:
        mas[i].append(mas[i + 1][1] - mas[i][1] - 1)
    else:
        mas[i].append(0)

del mas[-1]
res = [i for i in mas if i[2] == 13]

print(res[::-1])
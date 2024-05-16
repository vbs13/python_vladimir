mas = [x.strip() for x in open(input())]
del(mas[0])

mas2 = [[0 for y in range(int(mas[0]))] for x in range(int(mas[0]))]
del(mas[0])
# print(mas2)
for i in mas:
    q = (list(map(int, i.split())))
    mas2[int(i.split()[0]) - 1][int(i.split()[1]) - 1] = 1
mas3 = []
m = 0
m2 = 0
m3 = 0

for n in mas2:
    s = 0
    d = 0
    for i in n:
        if i == 1:
            s += 1
        else:
            if s >= 3:
                d += 1
            s = 0
    if s >= 3:
        d += 1
    m2 += 1
    if d > m:
        m = d
        m3 = m2
# print(mas3)
print(m, m3)
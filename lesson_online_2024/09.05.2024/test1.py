mas = [list(map(int, x.split(';'))) for x in open('9_16320.csv')]
print(mas)
k = 0
for n in mas:
    x = sorted(n)
    if x[3] < sum(x[:3]):
        if x[0] + x[3] == x[1] + x[2]:
            k += 1
print(k)
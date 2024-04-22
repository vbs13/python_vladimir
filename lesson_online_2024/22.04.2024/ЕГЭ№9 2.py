mas = [list(map(int, x.strip().split(';'))) for x in open('C:/Users/Владимир/Downloads/9_12918.csv')]
mas1 = []

for i in mas:
    if len(set(i)) == 4:
        if i.count(max(i)) == 1:
            if max(i) * min(i) > sum(i) - max(i) - min(i):
                mas1.append(i)
print(sum(mas1[0]))

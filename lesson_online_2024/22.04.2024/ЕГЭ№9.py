import csv

with open('C:/Users/Владимир/Downloads/9_15321.csv') as f:
    x = csv.reader(f, delimiter=';')
    k = 0

    for i in x:
        q = sorted(map(int, i))
        if q[3] < sum(q) - q[3]:
            if q[3] + q[0] == q[1] + q[2]:
                k += 1
print(k)
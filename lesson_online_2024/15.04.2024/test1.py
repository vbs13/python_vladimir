import csv


f = open('C:/Users/Владимир/Desktop/9_2101.csv', newline='')
a = csv.reader(f, delimiter=',')
k = 0

for i in a:
    q = sorted(map(int, i))
    if q[2]**2 < q[0]**2 + q[1]**2:
        k += 1

print(k)

def chet(mas):
    for n in mas:
        if n % 2 == 0:
            return False
    return True

f = open('f1.txt')
k = 0

for i in f:
    a = list(map(int, i.split()))
    # print(a)
    x = []
    y = []
    for n in a:
        if a.count(n) == 2:
            x.append(n)
        elif a.count(n) == 1:
            y.append(n)
    # print(x, y)
    if len(x) == 2 and len(y) == 4:
        if chet(y) and x[0] % 2 == 0:
            k += 1
print(k)



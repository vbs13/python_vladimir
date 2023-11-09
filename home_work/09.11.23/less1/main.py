mas = []

for n in range(0, 1001):
    a = bin(n)[2:]
    if a.count('1') % 2 == 0:
        a += '0'
        a = '10' + a[2:]
    elif a.count('1') % 2 != 0:
        a += '1'
        a = '11' + a[2:]
    r = int(a, 2)
    if r > 40:
        mas.append(n)

print(min(mas))

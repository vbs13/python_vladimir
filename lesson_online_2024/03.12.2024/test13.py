import itertools


x = itertools.product('0123456789ABCDEF', repeat=8)

k = 0
for i in x:
    a = ''.join(i)
    if a[0] != '0':
        if a.count('0') == 2:
            if (a.count('A') + a.count('B') + a.count('C') + a.count('D') + a.count('E') + a.count('F')) <= 4:
                k += 1

print(k)
import itertools


x = itertools.product('0123456789AB', repeat=5)

k = 0
for i in x:
    a = ''.join(i)
    if a[0] != '0':
        if a.count('7') == 1:
            if (a.count('9') + a.count('A') + a.count('B')) <= 3:
                k += 1
print(k)
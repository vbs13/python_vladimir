import itertools


x = itertools.product('АОУ', repeat=5)

k = 0
for i in x:
    k += 1
    a = ''.join(i)
    if a[0] == 'О':
        print(a, k)

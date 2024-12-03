import itertools

x = itertools.product('АОУ', repeat=5)

k = 0
for i in x:
    a = ''.join(i)
    k += 1
    if k == 210:
        print(a, k)
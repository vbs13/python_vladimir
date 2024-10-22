import itertools


a = itertools.product('0123456789ab', repeat=5)

k = 0
for i in a:
    q = ''.join(i)
    if q[0] != '0':
        if q.count('7') == 1:
            if q.count('9') + q.count('a') + q.count('b') <= 3:
                k += 1
print(k)

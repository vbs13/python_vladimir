import itertools

a = itertools.product('АПРСУ', repeat=5)

k = 0
for i in a:
    k += 1
    q = ''.join(i)
    if q.count('У') <= 1 and 'АА' not in q:
        print(k, q)
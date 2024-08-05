import itertools

a = itertools.product('АПРСУ', repeat=5)

c = 0
for i in a:
    c += 1
    q = ''.join(i)
    if q.count('У') == 1 and 'AA' not in q:
        print(c, q)
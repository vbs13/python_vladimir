import itertools


a = itertools.product('КЗБС', repeat=5)


k = 0
for i in a:
    q = ''.join(i)
    if q.count('З') <= 2:
        if ('КБ' not in q) and ('БК' not in q):
            k += 1
print(k)
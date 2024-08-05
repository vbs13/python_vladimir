import itertools

a = itertools.product('КОСУФ', repeat=5)

k = 0
for i in a:
    k += 1
    if 'Ф' not in i and i.count('У') == 2:
        print(k, i)
import itertools

a = [''.join(x) for x in list(itertools.product('УЧЕНИК', repeat=5))]

k = 0
for i in a:
    if i[0] == 'У' and i[-1] == 'К':
        k += 1
print(k)
import itertools


a = [''.join(x) for x in list(itertools.product(sorted('ФОКУС'), repeat=5))]

k = 0
for i in a:
    k += 1
    if 'Ф' not in i:
        if i.count('У') == 2:
            print(k, i)
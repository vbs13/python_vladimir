import itertools


a = [''.join(i) for i in list(itertools.product('ИВАН', repeat=5))]

k = 0
for i in a:
    if 'И' in i:
        k += 1
print(k)
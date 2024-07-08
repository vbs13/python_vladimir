import itertools


a = [''.join(i) for i in list(itertools.product('1234', repeat=5))]

k = 0
for i in a:
    if i.count('1') == 2:
        k += 1
print(k)

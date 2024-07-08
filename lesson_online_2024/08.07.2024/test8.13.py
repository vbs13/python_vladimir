import itertools


a = [''.join(x) for x in list(itertools.product('0123456', repeat=7))]

k = 0
for i in a:
    if i[0] != '0':
        if i.count('0') + i.count('2') + i.count('4') + i.count('6') == 2:
            k += 1
print(k)
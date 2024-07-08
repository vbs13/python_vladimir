import itertools


a = [''.join(x) for x in list(itertools.product('0123456789ABCDE', repeat=5))]

k = 0
for i in a:
    if i[0] != '0':
        if i.count('8') == 1:
            if (i.count('A') + i.count('B') + i.count('C') + i.count('D') + i.count('E')) >= 2:
                k += 1
print(k)
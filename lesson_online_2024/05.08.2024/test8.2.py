import itertools

a = itertools.product('0123456789ABCDE', repeat=5)

k = 0
for i in a:
    if i.count('8') == 1 and (i.count('A') + i.count('B') + i.count('C') + i.count('D') + i.count('E')) >= 2 and i[0] != '0':
        k += 1
print(k)
import itertools


a = itertools.product('012345678', repeat=7)

k = 0
for i in a:
    if i[0] != '0' and i[0] != '1' and i[0] != '3' and i[0] != '5' and i[0] != '7' and \
        i[-1] != '3' and i[-1] != '6' and i[-1] != '0' and i.count('6') >= 1:
        k += 1
print(k)
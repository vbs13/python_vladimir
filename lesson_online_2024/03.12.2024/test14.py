import itertools


x = itertools.product('012345678', repeat=5)

k = 0
for i in x:
    a = ''.join(i)
    if a[0] != '0':
        if a.count('3') == 2:
            if ('12' not in a) and ('21' not in a) and ('32' not in a) and ('23' not in a) and ('52' not in a)\
                and ('25' not in a) and ('72' not in a) and ('27' not in a):
                k += 1
print(k)
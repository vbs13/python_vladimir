import itertools


x = itertools.product('12', '34', '56')

for i in x:
    a = ''.join(i)
    print(a)
import itertools

x = itertools.permutations('МАТВЕЙ')

k = 0
for i in x:
    a = ''.join(i)
    if a[0] != 'Й':
        if 'АЕ' not in a:
            k += 1
print(k)
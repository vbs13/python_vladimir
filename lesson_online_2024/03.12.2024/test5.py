import itertools

x = itertools.product('ЕГЭ', repeat=5)

k = 0
for i in x:
    a = ''.join(i)
    if a[0] != 'Г':
        k += 1
print(k)
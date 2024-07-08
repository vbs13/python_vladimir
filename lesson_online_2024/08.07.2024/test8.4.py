import itertools

a = [''.join(x) for x in list(itertools.product('ЕГЭ', repeat=5))]

k = 0
for i in a:
    if i[0] != 'Г':
        k += 1
print(k)
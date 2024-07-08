import itertools

a = itertools.product('АКРУ', repeat=5)

k = 0
for i in a:
    k += 1
    x = ''.join(i)
    if x == 'РУКАА':
        print(k)
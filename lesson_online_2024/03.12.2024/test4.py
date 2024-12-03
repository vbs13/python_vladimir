import itertools

x = itertools.product(sorted('КОМПЬТЕР'), repeat=5)

k = 0
for i in x:
    k += 1
    a = ''.join(i)
    if a.count('К') == 0 and a.count('Р') == 2:
        print(k, a)
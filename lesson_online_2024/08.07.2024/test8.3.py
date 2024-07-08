import itertools


a = itertools.product(sorted('АЛГОРИТМ'), repeat=4)

k = 0
for i in a:
    k += 1
    x = ''.join(i)
    if x[:2] == 'ИГ':
        print(k, x)
        break

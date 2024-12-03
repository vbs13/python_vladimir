import itertools

x = itertools.permutations(sorted('ВИКТОР'))

k = 0
for i in x:
    k += 1
    a = ''.join(i)
    if k == 170:
        print(k, a)
import itertools


a =[''.join(x) for x in list(itertools.permutations('МУЖЧИНА', 6))]

k = 0
coun = 0
for i in a:
    if i[0] != 'Ч':
        if i.count('Ж') == 1:
            coun += 1
            if coun % 2 != 0:
                k += 1
print(k)
import itertools

a = [''.join(x) for x in list(itertools.product('01234567', repeat=5))]

k = 0
for i in a:
    if i[0] != '0':
        if int(i[0]) % 2 == 0:
            if i[-1] != '2' and i[-1] != '6':
                if i.count('7') <= 2:
                    k += 1
print(k)
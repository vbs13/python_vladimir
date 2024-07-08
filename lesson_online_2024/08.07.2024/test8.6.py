import itertools


a = [''.join(x) for x in list(itertools.product('ABCDXYZ', repeat=4))]

k = 0
for i in a:
    if 'X' in i[0] or 'Y' in i[0] or 'Z' in i[0]:
        if 'X' in i[1] or 'Y' in i[1] or 'Z' in i[1]:
            if 'A' in i[2] or 'B' in i[2] or 'C' in i[2] or 'D' in i[2]:
                if 'A' in i[3] or 'B' in i[3] or 'C' in i[3] or 'D' in i[3]:
                    k += 1
print(k)
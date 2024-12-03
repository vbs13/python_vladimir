import itertools

x = itertools.product('ABCDEXZ', repeat=4)

k = 0
for i in x:
    a = ''.join(i)
    if a[0] in 'XZ' and a[1] in 'XZ':
        if a[2] in 'ABCDE' and a[3] in 'ABCDE':
            k += 1
print(k)
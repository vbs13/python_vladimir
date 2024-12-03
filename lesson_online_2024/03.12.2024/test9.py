import itertools

x = itertools.product('012345', repeat=3)

k = 0
for i in x:
    a = ''.join(i)
    if a[0] != '0':
        if int(a[0]) >= int(a[1]) >= int(a[2]):
            k += 1
print(k)
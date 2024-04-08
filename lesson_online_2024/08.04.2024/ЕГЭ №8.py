import itertools

a = itertools.permutations('0123456789', 6)
# a = itertools.product('abc', repeat=5)
k = 0

for i in a:
    q = ''.join(i)
    if q[0] != '0' and int(q) % 5 == 0:
        if (int(q[0]) % 2 == 0 and int(q[1]) % 2 != 0 and int(q[2]) % 2 == 0 and int(q[3]) % 2 != 0 and int(q[4]) % 2 == 0 and int(q[5]) % 2 != 0) or \
            (int(q[0]) % 2 != 0 and int(q[1]) % 2 == 0 and int(q[2]) % 2 != 0 and int(q[3]) % 2 == 0 and int(q[4]) % 2 != 0 and int(q[5]) % 2 == 0):
            k += 1
print(k)

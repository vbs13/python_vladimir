import itertools

# a = itertools.permutations('abc')
#
# for i in a:
#     q = ''.join(i)
#     print(q)

a = itertools.product('abc', repeat=3)

for i in a:
    q = ''.join(i)
    print(q)
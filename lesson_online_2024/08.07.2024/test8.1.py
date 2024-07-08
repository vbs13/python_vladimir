# import itertools
#
#
# a = itertools.product('АОУ', repeat=5)
#
# k = 0
# for i in a:
#     k += 1
#     x = ''.join(i)
#     if k == 210:
#         print(k, x)


import itertools

a = list(itertools.product('АОУ', repeat=5))
b = [''.join(x) for x in a]
print(b[209])
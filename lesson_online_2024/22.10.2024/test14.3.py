def perev(x):
    res = ''
    while x > 0:
        res = res + str(x % 7)
        x //= 7
    return res


for x in range(0, 2031):
    if perev(7**170 + 7 **100 - x).count('0') == 71:
        print(x)
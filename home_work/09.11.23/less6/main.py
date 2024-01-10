def perev(a, s):
    alf = '01234'
    res = ''
    while a > 0:
        res = alf[(a % s)] + res
        a //= s

    return res

r = 7 * 5**123 + 6 * 5**111 - 5 * 25**50 + 4 * 125**30 - 3 * 5**10

print(perev(r, 5).count('4'))
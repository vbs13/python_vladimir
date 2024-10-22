def perev(a, s):
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUW'
    res = ''
    while a > 0:
        res = alf[(a % s)] + res
        a //= s

    return res

a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024
print(perev(a, 25).count('0'))

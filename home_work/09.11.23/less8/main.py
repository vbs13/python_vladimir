def perev(a, s):
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUW'
    res = ''
    while a > 0:
        res = alf[(a % s)] + res
        a //= s

    return res


for n in range(11, 1000):
    r = ''
    x = 0
    a = perev(n, 6)
    if (n % 3) == 0:
        r += a[0] + a[1] + a
    else:
        z = perev((n % 3) * 10, 6)
        r = a + z
    if int(r, 6) > 680:
        print(int(r, 6))
        break

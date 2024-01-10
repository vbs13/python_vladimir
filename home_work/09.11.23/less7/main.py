def perev(a, s):
    alf = '0123456789ABCDEFGHIJKLMNOPQRSTUW'
    res = ''
    while a > 0:
        res = alf[(a % s)] + res
        a //= s

    return res

for n in range(1, 1000):
    r = ''
    x = 0
    a = perev(n, 3)
    if (n % 2) == 0:
        r += '1' + a + '00'
    else:
        for i in range(len(a)):
            x += int(a[i])
        z = perev(x, 3)
        r = a + z
    if int(r, 3) > 168:
        print(n)
        break

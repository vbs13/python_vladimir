def summ(s):
    res = 0
    for i in s:
        res += int(i)
    return res

for n in range(4, 10001):
    s = '5' + '2' * n

    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if summ(s) == 64:
        print(n)


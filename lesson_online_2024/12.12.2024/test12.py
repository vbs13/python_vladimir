for n in range(3, 10001):
    s = '0' + '5' * n

    while '55' in s or '150' in s or '555' in s:
        if '55' in s:
            s = s.replace('55', '615', 1)
        if '150' in s:
            s = s.replace('150', '5950', 1)
        if '555' in s:
            s = s.replace('555', '50', 1)

    mas = [int(x) for x in s if int(x) % 2 != 0]
    a = 1
    for i in mas:
        a *= i
    if a > 100000:
        print(n)
        break

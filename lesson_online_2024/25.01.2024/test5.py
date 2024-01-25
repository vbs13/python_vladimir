def f(s):
    a = s
    while '00' not in s:
        s = s.replace('01', '210')
        s = s.replace('02', '320')
        s = s.replace('03', '3012')

    if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
        print(len(a))


for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            s = '0' + '1' * a + '2' * b + '3' * c + '0'
            f(s)

def per(x):
    res = ''
    while x > 0:
        n = x % 7
        res = str(n) + res
        x //= 7
    return res

for x in range(2030, 0, -1):
    y = 7 ** 91 + 7 ** 160 - x
    if per(y).count('0') == 70:
        print(x)
        break
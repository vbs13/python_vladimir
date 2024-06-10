def tr(x):
    res = 0
    while x > 0:
        if x % 3 == 0:
            res += 1
        x //= 3
    return res


for x in range(2030, -1, -1):
    a = 3 ** 100 - x
    if tr(a) == 5:
        print(x)
        break

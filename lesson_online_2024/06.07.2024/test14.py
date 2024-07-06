def re(x):
    res = 0
    while x > 0:
        if x % 6 == 0:
            res += 1
        x //= 6
    return res


for x in range(2030, 0, -1):
    if re(6**260 + 6**160 + 6**60  - x) == 202:
        print(x)
        break


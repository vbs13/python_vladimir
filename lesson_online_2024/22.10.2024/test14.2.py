def perev(x):
    res = 0
    while x > 0:
        if x % 25 == 0:
            res += 1
        x //= 25
    return res

print(perev(3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25 ** 4 - 2025))
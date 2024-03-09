def perev(n: int, s: int) -> str:
    res = ''
    while n > 0:
        res = str(n % s) + res
        n //= s
    return res


a = 361 * 2349 ** 84 - 89 ** 192 + 1953 ** 481 * 4843 ** 151
print(perev(a, 9).count('5'))
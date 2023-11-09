def ew(num, sys):
    res = ''
    alf = '0123456789abcdefghijklmno'
    while num > 0:
        res += alf[num % sys]
        num //= sys
    return res[::-1]


n = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024
print(n)
a = ew(n, 25)
print(a.count('0'))


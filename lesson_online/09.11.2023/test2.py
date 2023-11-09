def ew(num, sys):
    res = ''
    alf = '0123456789abcdef'
    while num > 0:
        res += alf[num % sys]
        num //= sys
    return res[::-1]

print(ew(194, 5))
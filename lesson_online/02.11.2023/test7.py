print(int('112', 3))
print(bin(76)[2:])
print(oct(76)[2:])
print(hex(76)[2:])


def f(n, s):
    res = ''
    alf = '0123456789abcdefghijklmnopq'
    while n > 0:
        res += alf[n % s]
        n //= s
    return res[::-1]


print(f(76, 2))
print(f(76, 8))
print(f(76, 16))
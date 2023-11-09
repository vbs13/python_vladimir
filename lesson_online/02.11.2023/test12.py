a = 16**2016 + 4**2015 - 64
res = ''
alf = '0123'
while a > 0:
    res += alf[a % 4]
    a //= 4
print(res[::-1].count('3'))
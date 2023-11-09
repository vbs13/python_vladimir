a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024
res = ''
alf = '0123456789abcdefghijklmno'
while a > 0:
    res += alf[a % 25]
    a //= 25
print(res[::-1].count('0'))

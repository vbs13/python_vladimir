a = int(input())
alf = '0123456789abcdef'
res = 0
s = ''

while a > 0:
    s = alf[(a % 15)] + s
    a //= 15
print(s)

for i in s:
    if i == 'a':
        res += 10
    elif i == 'b':
        res += 11
    elif i == 'c':
        res += 12
    elif i == 'd':
        res += 13
    elif i == 'e':
        res += 14
    elif i == 'f':
        res += 15
    else:
        res += int(i)
print(res)
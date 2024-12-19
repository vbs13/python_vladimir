f = open('24 (1).txt')
s = f.read()

x = ''
res = 0

for i in range(len(s) - 1):
    x = s[i]
    for j in s[i + 1:]:
        if j in x:
            res = max(res, len(x))
            break
        else:
            x += j
print(res)

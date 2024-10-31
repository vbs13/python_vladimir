f = open('24_2_demo.txt')
s = f.read()

m = 0
k = ''
for i in range(len(s)):
    if (k == '' or k[-1] == 'Z') and s[i] == 'X':
        k += s[i]
    elif k != '' and k[-1] == 'X' and s[i] == 'Y':
        k += s[i]
    elif k != '' and k[-1] == 'Y' and s[i] == 'Z':
        k += s[i]
    else:
        m = max(m, len(k))
        k = s[i]
m = max(m, len(k))
print(m)
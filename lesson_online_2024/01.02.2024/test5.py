n = int(input())
s = [list(map(int, input().split('*'))) for x in range(n)]

for i in range(len(s) - 1):
    if (s[i][0] * s[i][1] * s[i][2] > s[i + 1][0] * s[i + 1][1] * s[i + 1][2]):
        s[i], s[i + 1] = s[i + 1], s[i]
    elif (s[i][0] * s[i][1] * s[i][2] == s[i + 1][0] * s[i + 1][1] * s[i + 1][2])\
            and (s[i][0] > s[i + 1][0]):
        s[i], s[i + 1] = s[i + 1], s[i]
    elif (s[i][0] * s[i][1] * s[i][2] == s[i + 1][0] * s[i + 1][1] * s[i + 1][2])\
            and (s[i][0] == s[i + 1][0]) and (s[i][1] < s[i + 1][1]):
        s[i], s[i + 1] = s[i + 1], s[i]

for i in s:
    print('*'.join(list(map(str, i))))
f = open('24_demo.txt')
s = f.read()
print(s)

mas = []
k = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        k += 1
    else:
        mas.append(k)
        k = 1
mas.append(k)

print(max(mas))


# m = 0
# k = s[0]
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         k += s[i + 1]
#     else:
#         m = max(m, len(k))
#         k = s[i + 1]
# m = max(m, len(k))
# print(m)


# s = s.replace('XX', 'X X')
# s = s.replace('ZZ', 'Z Z')
# s = s.replace('YY', 'Y Y')
# s = s.replace('XX', 'X X')
# s = s.replace('ZZ', 'Z Z')
# s = s.replace('YY', 'Y Y')
# print(s)
# mas = s.split(' ')
# res = [len(x) for x in mas]
# print(max(res))

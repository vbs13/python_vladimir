f = open('zadanie24_1.txt')
s = f.read()


# m = 0
# k = ''
# for i in range(len(s) - 1):
#     if s[i] == 'B':
#         k += s[i]
#     else:
#         m = max(m, len(k))
#         k = ''
# m = max(m, len(k))
# print(m)


s = s.replace('A', ' ')
s = s.replace('C', ' ')
mas = s.split()
res = [len(x) for x in mas]
print(max(res))
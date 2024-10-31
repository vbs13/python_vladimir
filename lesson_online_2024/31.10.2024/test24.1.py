s = 'zyxyzyxxyzyyzyxyyzyxzyzxxyzy'
#
# mas = []
# k = 1
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         k += 1
#     else:
#         mas.append(k)
#         k = 1
# mas.append(k)
#
# print(mas)


# m = 0
# # k = s[0]
# # for i in range(len(s) - 1):
# #     if s[i] != s[i + 1]:
# #         k += s[i + 1]
# #     else:
# #         m = max(m, len(k))
# #         k = s[i + 1]
# # m = max(m, len(k))
# # print(m)


s = s.replace('xx', 'x x')
s = s.replace('zz', 'z z')
s = s.replace('yy', 'y y')
mas = s.split(' ')
res = [len(x) for x in mas]
print(max(res))
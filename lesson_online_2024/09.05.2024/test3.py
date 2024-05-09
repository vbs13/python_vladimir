f = open('24_16333.txt')
x = f.read()
# res = 0
#
# q = x[0]
# for i in x:
#     if i in ['Q', 'W', 'R'] and q[-1] in ['Q', 'W', 'R']:
#         res = max(len(q), res)
#         q = i
#     elif i in ['1', '2', '4'] and q[-1] in ['1', '2', '4']:
#         res = max(len(q), res)
#         q = i
#     else:
#         q += i
# print(res)

x = x.replace('Q', 'A').replace('W', 'A').replace('R', 'A')
x = x.replace('1', 'B').replace('2', 'B').replace('4', 'B')
x = x.replace('AA', 'A A').replace('BB', 'B B')
x = x.replace('AA', 'A A').replace('BB', 'B B')
res = x.split()
maxx = max([len(i) for i in res])
print(maxx)
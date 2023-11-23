s = 'aaaaabbbbbccccc'
print(s)

# strr = ''
# for i in s:
#     if i == 'b':
#         strr += 'e'
#     else:
#         strr += i
# print(strr)

strr = s.replace('b', 'e')
print(strr)

# flag = True
# strr2 = ''
# for i in s:
#     if i == 'b' and flag:
#         strr2 += 'e'
#         flag = False
#     else:
#         strr2 += i
# print(strr2)

strr2 = s.replace('b', 'e', 1)
print(strr2)


strr3 = s.replace('bc', '*')
print(strr3)
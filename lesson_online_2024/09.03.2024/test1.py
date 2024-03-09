f = open('24_4545.txt')
s = f.read()

# maxx = 0
# s = s.replace('Y', ' ').replace('Z', ' ')
# a = s.split()
# for i in a:
#     if maxx < len(i):
#         maxx = len(i)
# print(maxx)

# maxx = 0
# a = 0
# for i in range(len(s) - 1):
#     if s[i] == 'X':
#         a += 1
#         if s[i + 1] != 'X':
#             if a > maxx:
#                 maxx = a
#             a = 0
# print(maxx)

maxx = ''
a = ''
for i in s:
    if i == 'X':
        a += i
    else:
        if a > maxx:
            maxx = a
        a = ''
print(len(maxx))
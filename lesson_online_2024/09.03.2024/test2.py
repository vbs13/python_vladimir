f = open('24_4545.txt')
s = f.read()

# s = s.replace('XY', '*')
# s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
# a = s.split()
# maxx = 0
# for i in range(len(a)):
#     if maxx < len(a[i]):
#         maxx = len(a[i])
# print(maxx)

a = ''
maxx = ''
for i in s:
    if i == 'X' and (a == '' or a[-1] == 'Z'):
        a += i
    elif i == 'Y' and a != '' and a[-1] == 'X':
        a += i
    elif i == 'Z' and a != '' and a[-1] == 'Y':
        a += i
    else:
        if len(a) > len(maxx):
            maxx = a
        a = i   
print(len(maxx))
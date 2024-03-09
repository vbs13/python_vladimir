f = open('24_12931.txt')
s = f.read()

maxx = ''
a = ''
for i in s:
    if i == 'V' and (a == '' or a[-1] == 'Z'):
        a += i
    elif i == 'W' and (a == '' or a[-1] == 'V'):
        a += i
    elif i == 'X' and (a == '' or a[-1] == 'W'):
        a += i
    elif i == 'Y' and (a == '' or a[-1] == 'X'):
        a += i
    elif i == 'Z' and (a == '' or a[-1] == 'Y'):
        a += i
    else:
        if len(a) > len(maxx):
            maxx = a
        a = i
print(len(maxx))
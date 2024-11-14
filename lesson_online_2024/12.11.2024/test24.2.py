f = open('C:/Users/Владимир/Downloads/24_18147 (1).txt')
s = f.read()

s = s.replace('*', ' ')
s = s.replace('++', ' ')
while '+ ' in s:
    s = s.replace('+ ', ' ')
while ' +' in s:
    s = s.replace(' +', ' ')

mas = s.split()
res = [x for x in mas if '+' in x]
m = 0
for i in res:
    res1 = i.split('+')
    res2 = sum(list(map(int, res1)))
    m = max(m, res2)
print(m)
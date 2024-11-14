f = open('C:/Users/Владимир/Downloads/24_17641.txt')
s = f.read()

for i in '123456789':
    s = s.replace(i, '1')

while ' 01' in s or '*01' in s or '+01' in s:
    s = s.replace(' 01', ' 0 1')
    s = s.replace('*01', '*0 1')
    s = s.replace('+01', '+0 1')

s = s.replace('**', ' ').replace('++', ' ').replace('*+', ' ').replace('+*', ' ')
# s = s.replace('+1', '+ 1')
# s = s.replace('1+', '1 +')

while '* ' in s or '+ ' in s:
    s = s.replace('* ', ' ').replace('+ ', ' ')
while ' *' in s or ' +' in s:
    s = s.replace(' *', ' ').replace(' +', ' ')

mas = s.split()
mas2 = sorted(mas, key=len)
m = []
for i in mas2:
    m.append(i)

for i in m:
    print(len(i), i, eval(i))

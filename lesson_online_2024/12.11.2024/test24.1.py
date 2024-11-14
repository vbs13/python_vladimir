f = open('C:/Users/Владимир/Downloads/24_18619.txt')
s = f.read()

s = s.replace('A', ' ').replace('C', ' ').replace('D', ' ')
s = s.replace('B', ' B')
s = s.replace('*', '-')
s = s.replace('--', '- -')
s = s.replace('B-', 'B -')
s = s.replace('- ', ' ')
mas = s.split()
res = [x for x in mas if x[0] == 'B']

m = ''
for i in res:
    if len(i) > len(m):
        m = i
print(m, len(m))
f = open('C:/Users/Владимир/Downloads/24_18147.txt')
s = f.read()

m = 0
s = s.replace('*', ' ')
s = s.replace('++', ' ')
mas = s.split()
for i in mas:
    q = i.replace('+', ' ')
    a = q.split()
    if len(a) > 1:
        summ = 0
        for y in a:
            summ += int(y)
        m = max(m, summ)
m = max(m, summ)
print(m)


f = open('24_19254.txt')
s = f.read()


s = s.replace('FSRQ', ' ').split(' ')
mas = [len(x) for x in s]

k = 0
for i in range(len(mas)):
    c = sum(mas[i: i + 81])
    k = max(k, c)
print(k + 80 * 4)



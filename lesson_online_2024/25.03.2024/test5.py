f = open('26_12256.txt')
s = f.readlines()
del s[0]
st = sorted(list(map(int, s)))

mas = []
for i in st:
    if sum(mas) + i <= 9800:
        mas.append(i)
print(len(mas))

m = 0
delta = 9800 - sum(mas) + max(mas)
for i in st:
    if delta >= i:
        m = max(m, i)

print(m)
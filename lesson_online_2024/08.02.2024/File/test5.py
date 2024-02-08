f = open('C:/Users/Владимир/Downloads/17.txt')
t = f.readlines()
a = list(map(int, t))


k = []
for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        k.append(a[i] + a[i + 1])

print(a)
print(len(k))
print(max(k))
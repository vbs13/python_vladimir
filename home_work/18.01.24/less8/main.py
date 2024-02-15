n = int(input())
mas = []
res = []

for i in range(n):
    mas.append(i)

for i in range(n):
    if i % 2 == 0 or i == 0:
        res.append(1)
    else:
        res.append(mas[i] % 5)
print(res)

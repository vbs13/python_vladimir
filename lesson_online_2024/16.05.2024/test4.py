n = int(input())
mas = []
for i in range(n):
    mas.append(input().split())

mas1 = mas[0]
l = len(mas[0])
for i in mas:
    if len(i) < l:
        mas1 = i
        l = len(i)

res = []
for elem in mas1:
    flag = True
    for x in mas:
        if elem not in x:
            flag = False
    if flag == True:
        res.append(elem)


if res == []:
    print('NO')
else:
    print(*sorted(res))

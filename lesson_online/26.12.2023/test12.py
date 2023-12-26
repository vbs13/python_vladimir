text = input('Введите текст: ')
res = {}

for i in text:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1
print(res)

maxx = 0
for i in res:
    # if maxx < res[i]:
    #     maxx = res[i]
    maxx = max(maxx, res[i])

for i in res:
    if res[i] == maxx:
        print(i, '-', maxx)
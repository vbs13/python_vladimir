mas = [int(x) for x in open('26_16335.txt')]
del mas[0]
mas.sort(reverse=True)
k = 4
cake = [mas[0]]
del mas[0]

for i in mas:
    if cake[-1] - i >= k:
        cake.append(i)
print(len(cake), cake[-1])
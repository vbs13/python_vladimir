from math import ceil


mas = [int(x) for x in open('inf_22_10_20_26 (1).txt')]
del mas[0]

summ = 0
for i in mas:
    if i <= 100:
        summ += i
print(summ)

summ1 = 0
mas1 = sorted([i for i in mas if i > 100])
for i in range(len(mas1) // 2):
    summ1 += mas1[i]

res = ceil(summ1 * 0.7)
for i in range(len(mas1) // 2, len(mas1)):
    res += mas1[i]
    
res += summ

print(res, mas1[len(mas1) // 2])
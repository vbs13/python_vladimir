summ = 0
kol = 0
while True:
    a = int(input())
    if a == 0:
        break
    elif a % 2 == 0 and a % 5 == 0:
        summ += a
        kol += 1

print(summ/kol, summ, kol)
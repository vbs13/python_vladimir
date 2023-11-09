def task1(n):
    a = n % 10
    b = n // 10 % 10
    c = n // 100 % 10
    d = n // 1000

    summ1 = d + c
    summ2 = a + b

    return str(min(summ1, summ2)) + str(max(summ1, summ2))


num = 0
for i in range(1000, 10000):
    if task1(i) == '616':
        if (i // 1000) % 2 != 0 and (i //100 % 10) % 2 != 0 and (i //10 % 10) % 2 != 0 and (i % 10) % 2 != 0:
            num += 1
print(num)
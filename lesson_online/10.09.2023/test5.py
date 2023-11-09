def task(n):
    a = n % 10
    b = n // 10 % 10
    c = n // 100

    summ1 = c + b
    summ2 = a + b

    x = max(summ2, summ1)
    y = min(summ2, summ1)

    res = str(x) + str(y)
    return res


for i in range(100, 1000):
    if task(i) == '1412':
        print(i)
        break
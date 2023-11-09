k = 0
for n in range(1000, 10000):
    a = n // 1000
    b = n // 100 % 10
    c = n // 10 % 10
    d = n % 10

    n1 = a + b
    n2 = c + d

    maxX = str(max(n1, n2))
    minN = str(min(n1, n2))

    res = minN + maxX

    if (res == '616') and (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0) and (d % 2 != 0):
        k += 1

print(k)
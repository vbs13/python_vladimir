def func(x):
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            return False
    return True

k = 1
for n in range(2422000, 2422081):
    if func(n):
        print(k, n)
        k += 1
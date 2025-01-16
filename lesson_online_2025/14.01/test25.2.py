def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return i + x // i
    return 0

for i in range(900000, 1200000):
    if f(i) % 100 == 46:
        print(i, f(i))


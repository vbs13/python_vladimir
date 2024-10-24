def func(x):
    mas = set()
    for n in range(1, int(x ** 0.5) + 1):
        if x % n == 0:
            mas.add(n)
            mas.add(x // n)
    return mas


for n in range(1000, 10000):
    s = sum(func(n))
    if s % 100 == 23:
        print(n, s)
def func(x):
    mas = set()
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            mas.add(n)
            mas.add(x // n)
    return mas


for n in range(900000, 1000001):
    if len(func(n)) != 0:
        m = max(func(n)) + min(func(n))
        if m % 100 == 46:
            print(n, m)
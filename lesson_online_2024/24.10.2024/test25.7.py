def func(x):
    mas = set()
    for n in range(1, int(x ** 0.5) + 1):
        if x % n == 0:
            if n % 2 == 0:
                mas.add(n)
            if (x // n) % 2 == 0:
                mas.add(x // n)
            if len(mas) >= 4:
                return mas
    return mas


for n in range(101000000, 102000001):
    if len(func(n)) == 3:
        print(n)
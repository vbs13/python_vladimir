def func(x):
    mas = set()
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            if n != 7 and n % 10 == 7:
                mas.add(n)
            if (x // n) != 7 and (x // n) % 10 == 7:
                mas.add(x // n)
    return mas

k = 1
for n in range(700000, 800001):
    if len(func(n)) > 0:
        print(n, min(func(n)))
        k += 1
        if k > 5:
            break

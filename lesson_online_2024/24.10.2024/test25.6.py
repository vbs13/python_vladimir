def func(x):
    mas = set()
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            mas.add(n)
            mas.add(x // n)
            if len(mas) >= 3:
                break
    return mas


for n in range(174457, 174506):
    if len(func(n)) == 2:
        print(sorted(func(n)))
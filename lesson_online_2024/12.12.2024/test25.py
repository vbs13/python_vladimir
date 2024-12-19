def f(x):
    k = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            k.add(i)
            k.add(x // i)
    return k


for i in range(700000, 1000000):
    if len(f(i)) == 2:
        if (max(f(i)) - min(f(i))) <= 15:
            print(i, (max(f(i)) - min(f(i))))

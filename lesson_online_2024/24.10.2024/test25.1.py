def func(x):
    mas = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            mas.add(i)
            mas.add(x // i)
    return mas

print(func(16), len(func(16)))


def f(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


print(f(12))

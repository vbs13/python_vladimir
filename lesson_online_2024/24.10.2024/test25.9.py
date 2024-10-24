def prost(x):
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            return False
    return True


def func(x):
    mas = set()
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            if prost(n):
                mas.add(n)
            if prost(x // n):
                mas.add(x // n)
            if len(mas) >= 4:
                return mas
    return mas


for n in range(1000000, 2000001):
    if len(func(n)) == 3:
        print(n, max(func(n)))
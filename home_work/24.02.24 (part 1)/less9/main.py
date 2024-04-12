def f(x, y):
    a = 0
    if x > y:
        return 0
    if x == 100:
        return 0
    if x == y:
        return 1
    if x % 10 != 0:
        a += f(x + x % 10, y)
    if x % 68 != 0:
        a += f(x + x % 68, y)
    a += f(x ** 2, y)
    return a

print(f(2, 68) * f(68, 680))
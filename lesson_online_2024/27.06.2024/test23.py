def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return f(x - 2, y) + f(x // 2, y)

print(f(32, 8) * f(8, 1))

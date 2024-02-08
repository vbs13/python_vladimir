def f(x, y):
    if x < y or x == 5:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 1, y) + f(x // 2, y)


print(f(45, 15) * f(15, 3))
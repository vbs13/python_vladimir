def f(x):
    if x == 1:
        return 1
    else:
        return 2 * g(x - 1) + 5 * x


def g(x):
    if x == 1:
        return 1
    else:
        return f(x - 1) + 2 * x


print(f(4) + g(4))
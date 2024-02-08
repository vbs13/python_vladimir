def f(x, y):
    if x > y or x == 4:
        return 0
    elif x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y)


print(f(2, 7))
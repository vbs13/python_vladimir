def f(x):
    if x == 0:
        return 0
    elif x % 3 == 2:
        return f(x - 1) + 1
    elif x % 3 < 2:
        return f((x - (x % 3)) / 3)

print(f(5))
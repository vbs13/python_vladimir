def f(x):
    if x == 1:
        return 3
    else:
        return f(x - 1) * (x - 1)


print(f(6))
def f(x):
    if x == 1:
        return 1
    else:
        return f(x - 1) + 2**(x - 1)


print(f(12))
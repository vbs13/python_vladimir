def f(x):
    if x == 1 or x == 2:
        return 5
    else:
        return 5 * f(x - 1) - 4 * f(x - 2)

print(f(13))
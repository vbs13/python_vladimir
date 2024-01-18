def f(x):
    if x <= 5:
        return x
    else:
        return 2*x - 8 + f(x - 2) + f(x - 1) // 8


print(f(50))
import sys


sys.setrecursionlimit(2029)

def f(x):
    if x <= 3:
        return 1
    else:
        return (x + 3) * f(x - 2)


print(f(2028) / f(2024))
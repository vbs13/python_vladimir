import sys


sys.setrecursionlimit(2026)
def f(x, y):
    if x == y:
        return 1
    elif x == 42 or x < y:
        return 0
    else:
        return f(x - 1, y) + f(x // 3, y) + f(x // 4, y)

print(f(2025, 250) * f(250, 25))

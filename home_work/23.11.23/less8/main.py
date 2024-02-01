import sys


sys.setrecursionlimit(2025)

def f(x):
    if x < 7:
        return 7
    else:
        return 2 * x + f(x - 1)

print(f(2024) - f(2022))
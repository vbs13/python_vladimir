import sys
sys.setrecursionlimit(2028)

def f(n):
    if n <= 3:
        return 5
    else:
        return 3 * (n - 1) * f(n - 2)

print(f(2027) // f(2023))
import sys
sys.setrecursionlimit(2025)
def f(n):
    if n == 1:
        return 1
    else:
        return 2 * n * f(n - 1)

print((f(2024)//16 - f(2023))/f(2022))
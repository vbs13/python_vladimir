import sys
from functools import*

sys.setrecursionlimit(5000)
@lru_cache(None)
def f(x, y):
    res = 0
    if x > y or x == 100:
        return 0
    if x == y:
        return 1
    if x % 10 != 0:
        res += f(x + x % 10, y)
    if x % 68 != 0:
        res += f(x + x % 68, y)
    res += f(x**2, y)
    return res

print(f(2, 68) * f(68, 680))
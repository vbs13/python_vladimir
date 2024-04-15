import sys
from functools import*

sys.setrecursionlimit(5000)
def summ(x):
    res = 0
    x = str(x)
    for i in x:
        res += int(i)
    return res
@lru_cache(None)
def f(x, y):
    res = 0
    if x > y:
        return 0
    if x == y:
        return 1
    if x % 10 != 0:
        res += f(x + x % 10, y)
    if (int(str(x)[0]) * x) > x:
        res += f(x * int(str(x)[0]), y)
    res += f(x * 2 + summ(x), y)
    return res

print(f(10, 4096))
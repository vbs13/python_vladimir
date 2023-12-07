def fact(a, b):
    res = 1
    for i in range(a, b + 1):
        res *= i
    return res


n = int(input())
k = int(input())

c = fact(n - k + 1, n) / fact(1, k)
print(c)
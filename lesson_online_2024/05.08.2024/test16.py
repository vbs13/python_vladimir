# import sys
# sys.setrecursionlimit(2025)
# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return n * f(n - 1)
#
# print((f(2024) - f(2023)) / f(2022))


f = {}
for n in range(1, 2025):
    if n == 1:
        f[n] = 1
    elif n > 1:
        f[n] = n * f[n - 1]
print((f[2024] - f[2023]) / f[2022])
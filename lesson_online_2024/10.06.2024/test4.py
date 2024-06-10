# import sys
# sys.setrecursionlimit(3000)
#
#
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n * f(n - 1)
#
# print((2 * f(2024) + f(2023)) / f(2022))


f = {1: 1}
for i in range(2, 2025):
    f[i] = i * f[i - 1]
print((2 * f[2024] + f[2023]) / f[2022])
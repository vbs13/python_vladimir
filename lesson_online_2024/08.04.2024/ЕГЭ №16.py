# import sys
#
# sys.setrecursionlimit(2025)
# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1:
#         return n - 2 + f(n - 1)
#
# print(f(2024) - f(2022))


n = {1: 1}
for i in range(2, 2025):
    n[i] = i - 2 + n[i - 1]
print(n[2024] - n[2022])
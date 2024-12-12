# import sys
#
#
# sys.setrecursionlimit(2026)
# def f(n):
#     if n >= 2025:
#         return 1
#     else:
#         return n - f(n + 2) - f(n + 4)
#
# print(f(20) + f(25))


mas = {}

for n in range(2500, 0, -1):
    if n >= 2025:
        mas[n] = 1
    else:
        mas[n] = n - mas[n + 2] - mas[n + 4]
print(mas[20] + mas[25])
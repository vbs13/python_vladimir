# for x in range(-100, 100):
#     def f(n):
#         if n >= 3000:
#             return n
#         return n + x + f(n + 2)
#     if f(2984) - f(2988) == 5916:
#         print(x)


for x in range(-100, 100):
    n = {}
    for i in range(3500, 1, -1):
        if i >= 3000:
            n[i] = i
        else:
            n[i] = i + x + n[i + 2]
    if n[2984] - n[2988] == 5916:
        print(x)
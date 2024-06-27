def re(x):
    res = 0
    while x > 0:
        if x % 6 == 0:
            res += 1
        x //= 6
    return res


mas = []
for x in range(1, 2031):
    y = 6 ** 2030 + 6 ** 100 - x
    mas.append(re(y))
print(max(mas))
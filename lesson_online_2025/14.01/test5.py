def perev(x):
    res = ''
    while x > 0:
        res = str(x % 3) + res
        x //= 3
    return res

mas = []
for n in range(1, 1000):
    b = perev(n)

    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + perev(b.count('1') + 2 * b.count('2'))

    r = int(b, 3)
    if (r > 220) and (r % 2 == 0):
        mas.append(r)
print(min(mas))
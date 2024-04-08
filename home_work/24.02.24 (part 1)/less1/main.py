def fun(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s


def summ(x):
    res = 0
    for i in x:
        res += int(i)
    return res

mas = []
for n in range(10, 10000):
    w = fun(n)

    if summ(w) % 4 == 0:
        w = '1' + w
        w = w[:-2]
    else:
        w = w + fun((summ(w) % 4) * 3)

    r = int(w, 3)
    if r > 353:
        mas.append(r)

print(min(mas))
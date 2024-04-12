for x in range(-100, 100):
    f =
    for n in range(2, 3004):
        if n >= 3000:
            f[n] = n
        else:
            f[n] = n + x + f[n + 2]
    if f[2984] - f[2988] == 5916:
        print(x)
# ??
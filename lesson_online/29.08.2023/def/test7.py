def ob(r):
    a = 4/3 * 3.14 * r**3
    return a


def per(r):
    b = 4 * 3.14 * r**2
    return b


for i in range(1, 5):
    print('радиус:', i, 'обьём:', ob(i), 'периметр:', per(i))

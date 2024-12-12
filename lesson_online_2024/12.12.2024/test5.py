for n in range(1000, 10000):

    mas = [int(x) for x in str(n)]
    a = sum([x for x in mas if x % 2 == 0]) ** 2
    b = (max(mas) - min(mas)) ** 3
    res = str(min(a, b)) + str(max(a, b))
    if res == '4343':
        print(n)
        break
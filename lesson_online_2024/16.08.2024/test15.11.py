k = 0
for a in range(-1000, 1000):
    for x in range(-300, 300):
        for y in range(-300, 300):
            if (((a < x) or (x ** 2 - 7 * x + 10 > 0)) and ((a >= y) or (y ** 2 + 7 * y + 12 > 0))) == 0:
                break
        else:
            continue
        break
    else:
        print(a)


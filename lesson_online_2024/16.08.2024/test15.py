for a in range(1000):
    for x in range(500):
        for y in range(500):
            if ((not((2 * x) < (2 * a + 3 * y))) or (y < 5) or (y >= 18) or (x < 87)) == 0:
                break
        else:
            continue
        break
    else:
        print(a)
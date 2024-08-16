for a in range(1000):
    for x in range(500):
        for y in range(500):
            if (((y + 2 * x) < a) or (x > 30) or (y > 20)) == 0:
                break
        else:
            continue
        break
    else:
        print(a)
        break
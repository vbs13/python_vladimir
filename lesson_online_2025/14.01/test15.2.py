for a in range(0, 500):
    for x in range(1, 500):
        for y in range(1, 500):
            if (((x - 3 * y) < a) or (y > 400) or (x > 56)) == 0:
                break
        else:
            continue
        break
    else:
        print(a)
        break
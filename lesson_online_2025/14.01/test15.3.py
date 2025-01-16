for a in range(0, 500):
    for x in range(1, 500):
        for y in range(1, 500):
            if ((x - y >= 39) or (y <= x) or (y >= a - 20)) == 0:
                break
        else:
            continue
        break
    else:
        print(a)

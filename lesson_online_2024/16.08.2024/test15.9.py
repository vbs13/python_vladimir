for a in range(1000):
    for x in range(500):
        for y in range(500):
            if (((x + y) <= 24) or (y <= (x - 2)) or (y >= a)) == 0:
                break
        else:
            continue
        break
    else:
        print(a)
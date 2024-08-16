for a in range(1000):
    for x in range(500):
        if (((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & a != 0))) == 0:
            break
    else:
        print(a)
        break   
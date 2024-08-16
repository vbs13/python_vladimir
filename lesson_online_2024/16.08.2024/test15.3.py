for a in range(1000):
    for x in range(500):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) == 0:
            break
    else:
        print(a)
        break
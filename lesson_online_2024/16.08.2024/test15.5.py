for a in range(1000):
    for x in range(500):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))) == 0:
            break
    else:
        print(a)
        break
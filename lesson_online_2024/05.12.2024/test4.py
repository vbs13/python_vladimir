for a in range(0, 1001):
    for x in range(0, 1001):
        if (((x & 116 != 0) or (x & 92 != 0)) <= ((x & 69 == 0) <= (x & a != 0))) == 0:
            break
    else:
        print(a)
        break
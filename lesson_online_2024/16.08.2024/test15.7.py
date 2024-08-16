for a in range(1000):
    for x in range(1, 501):
        for y in range(1, 501):
            if (((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))) == 0:
                break
        else:
            continue
        break
    else:
        print(a)
for p in range(10, 36):
    for x in range(0, p):
        for y in range(0, p):
            n1 = 9 * p**0 + x * p**1 + 4 * p**2 + 2 * p**3
            n2 = 3 * p**0 + y * p**1 + x * p**2 + y * p**3
            n3 = 0 * p**0 + y * p**1 + 4 * p**2 + x * p**3
            if n1 + n2 == n3:
                print(x, y, p)
                print(y * p**0 + y * p**1 + x * p**2)
                print(int(str(x) + str(y) + str(y), p))
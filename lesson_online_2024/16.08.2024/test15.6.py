def dell(n, m):
    return n % m == 0


for a in range(1000):
    for x in range(1, 501):
        if ((dell(72, x)) <= (not(dell(120, x))) or (a - x > 100)) == 0:
            break
    else:
        print(a)
        break
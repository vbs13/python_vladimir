def dell(n, m):
    return n % m == 0


for a in range(1, 1001):
    for x in range(1, 301):
        if ((a < 50) and ((not(dell(x, a))) <= (dell(x, 10) <= (not(dell(x, 12)))))) == 0:
            break
    else:
        print(a)
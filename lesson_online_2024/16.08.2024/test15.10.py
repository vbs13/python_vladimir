def dell(n, m):
    return n % m == 0


for a in range(1, 1001):
    for x in range(1, 501):
        if ((not(dell(x, a))) <= (dell(x, 28) <= (not(dell(x, 49))))) == 0:
            break
    else:
        print(a)
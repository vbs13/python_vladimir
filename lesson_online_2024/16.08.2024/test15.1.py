def dell(n, m):
    return n % m == 0


for a in range(1, 1001):
    for x in range(1, 301):
        if ((not(dell(x, a))) <= (dell(x, 6) <= (not(dell(x, 4))))) == 0:
            break
    else:
        print(a)

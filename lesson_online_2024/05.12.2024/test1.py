def dell(x, y):
    return x % y == 0


for a in range(1, 1001):
    for x in range(1, 1001):
        if ((not(dell(x, a))) <= (dell(x, 6) <= (not(dell(x, 4))))) == False:
            break
    else:
        print(a)
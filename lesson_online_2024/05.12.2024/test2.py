def dell(x, y):
    return x % y == 0


for a in range(0, 501):
    for x in range(1, 501):
        if ((dell(72, x) <= (not(dell(90, x)))) or (a - x > 80)) == False:
            break
    else:
        print(a)
        break
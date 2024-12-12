def dell(x, y):
    return x % y == 0


for a in range(1, 501):
    for x in range(0, 501):
        if (((not(dell(x, 100))) and dell(x, 4)) or dell(x, 400) or (not(dell(x, a)))) == 0:
            break
    else:
        print(a)
        break

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (((x <= y) and (y <= w)) or (z == (x or y)))
                if f == False:
                    print(x, y, z, w)

print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (y <= (x or z)) and (z <= y)
                if f == 0:
                    print(x, y, z, w, int(f))

print('w z y x')
for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                f = (x and (not(y))) or (y == z) or (not(w))
                if f == False:
                    print(w, z, y, x)
print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (y <= (not(x <= z)) or w)
                if f == False:
                    print(w, x, y, z, int(f))
print('x y w z f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not(((((((w and x)  == x) or 1) <= z) or (not(x))) and y)))
                if f == False:
                    print(x, y, w, z)

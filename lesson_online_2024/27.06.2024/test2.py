print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w)))
                if f:
                    print(w, x, y, z, int(f))
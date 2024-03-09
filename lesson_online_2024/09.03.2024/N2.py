print('p y h n')
for p in range(2):
    for y in range(2):
        for h in range(2):
            for n in range(2):
                f = (y and (not(y or h)) or (not(y <= h)) and (n <= p))
                if f:
                    print(p, y, h, n)

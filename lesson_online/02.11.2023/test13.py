for n in range(128, 256):
    m = bin(n)[2::]
    a = str(m)
    for i in a:
        if i == '1':
            i = '.'
        if i == '0':
            i = '1'
        if i == '.':
            i = '0'

    b = int(a, 2)
    if (b - n) == 185:
        print(n)

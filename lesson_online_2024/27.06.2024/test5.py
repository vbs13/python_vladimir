for n in range(1000, 0, -1):
    b = bin(n)[2::]
    summ = b.count('1')
    b += str(summ % 2)
    summ = b.count('1')
    b += str(summ % 2)
    r = int(b, 2)
    if r > 123:
        print(r)

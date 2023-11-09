for n in range(2, 10000):

    a = bin(n)[2:]
    chet = str(a[::2]).count('1')
    nechet = str(a[1::2]).count('0')

    modr = max(chet, nechet) - min(chet, nechet)

    if modr == 5:
        print(n)


print(bin(511))
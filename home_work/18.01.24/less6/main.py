for x in '0123456789ABCDEFGHIJKLM':
    x = int('7' + x + '38596', 23) + int('14' + x + '36', 23) + int('61' + x + '7', 23)
    if x % 22 == 0:
        print(x // 22)
        break
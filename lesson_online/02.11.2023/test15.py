for x in '0123456789abcd':
    for y in '0123456789abcdefg':
        a = int(f'8{x}78{y}', 13)
        b = int(f'79{x}{y}7', 17)
        if (a + b) % 9 == 0:
            print(x, y)
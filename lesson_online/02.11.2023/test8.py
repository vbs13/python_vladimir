for x in '0123456789abcdefg':
    a = int(f'7ac{x}53d', 17)
    b = int(f'83BG94{x}D', 17)
    c = int(f'C5{x}D', 17)
    d = int(f'C4BBF{x}4', 17)
    e = int(f'7{x}79', 17)
    if (a + b + c + d + e) % 16 == 0:
        print(x, (a + b + c + d + e) // 16)

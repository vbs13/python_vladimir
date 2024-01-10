alf = '0123456789ABCDEFG'
a = 0
for x in alf:
    a = int('7AC' + x + '53D', 17)
    b = int('83BG94' + x + 'D', 17)
    c = int('C5' + x + 'D', 17)
    d = int('C4BBF' + x + '4', 17)
    e = int('7' + x + '79', 17)
    if ((a + b + c + d + e) % 16) == 0:
        print(x, (a + b + c + d + e) / 16)


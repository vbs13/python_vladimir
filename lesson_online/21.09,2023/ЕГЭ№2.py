alf = '0123456789ABCDEFGHI'
for x in alf:
    a = int('98897' + x + '21', 19)
    b = int('2' + x + '923', 19)
    if ((a + b) % 18) == 0:
        print((a + b) // 18)



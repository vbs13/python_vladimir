alf = '0123456789ABCDEFGHIJKLMNO'
for x in alf:
    f = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if f % 24 == 0:
        print(x, f // 24)
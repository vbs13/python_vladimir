alf = '0123456789abc'
for x in alf:
    a = int(f'8{x}71', 13)
    b = int(f'3{x}df', 17)
    if (a + b) % 197 == 0:
        print(x, (a + b)/197)

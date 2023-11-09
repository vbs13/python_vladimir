for s in range(0, 10000):
    for x in '012345678':
        a = int(f'842{x}5', 9)
        b = int(f'8{x}725', 9)
        if (a + s) % b == 0:
            print(s)


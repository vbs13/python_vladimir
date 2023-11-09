for x in '0123456789a':
    for y in '0123456789a':
        a = int(f'{x}341{y}', 11)
        b = int(f'56{x}1{y}', 19)
        if (a + b) % 305 == 0:
                print(x, y, (a + b)/ 305)

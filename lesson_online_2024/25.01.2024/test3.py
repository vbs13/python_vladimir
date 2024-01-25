for n in range(1000, 10000):
    a = n // 1000
    b = n // 100 % 10
    c = n // 10 % 10
    d = n % 10

    ab = a + b
    bc = b + c
    cd = c + d
    mas = [ab, bc, cd]
    mas.remove(min(ab, bc, cd))

    res = str(min(mas)) + str(max(mas))
    if int(res) == 1215:
        print(n)
a = 0
for n in range(38000000, 100000000000000000000):
    x = bin(n)[2::]

    if n % 3 == 1 or n % 3 == 0:
        x += '0' + str(bin(n % 3)[2::])
    else:
        x += str(bin(n % 3)[2:])
    y = int(x, 2)

    if y % 5 == 0 or y % 5 == 1:
        x += '00' + str(bin(y % 5)[2::])
    elif y % 5 == 2 or y % 5 == 3:
        x += '0' + str(bin(y % 5)[2::])
    else:
        x += str(bin(y % 5)[2:])

    r = int(x, 2)
    print(r)
    if r in range(1222222222, 1555555667):
        a += 1
    if r > 1555555667:
        break
print(a)

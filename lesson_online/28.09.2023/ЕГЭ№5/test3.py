b = []

for n in range(1, 1000):
    a = bin(n)[2:]
    if n % 2 == 0:
        a += '00'
    else:
        a += '11'
    r = int(a, 2)
    if r > 115:
        b.append(n)

print(min(b))
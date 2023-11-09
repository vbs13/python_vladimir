b = []

for n in range(1, 1000):
    a = bin(n)[2:]
    a += str(a.count('1') % 2)
    a += str(a.count('1') % 2)
    r = int(a, 2)
    if r > 43:
        b.append(r)

print(min(b))
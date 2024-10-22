mas = []
for n in range(195, 1001):
    b = bin(n)[2:]

    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + bin(3 * (n % 3))[2:]
    r = int(b, 2)
    mas.append(r)
print(min(mas))
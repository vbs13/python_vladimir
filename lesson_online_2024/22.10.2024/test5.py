mas = []

for n in range(0, 13):
    b = bin(n)[2:]

    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'

    mas.append(int(b, 2))
print(max(mas))

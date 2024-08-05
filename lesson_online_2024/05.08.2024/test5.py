mas = []
for n in range(1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'

    r = int(b, 2)
    if r > 516:
        mas.append(n)
print(min(mas))
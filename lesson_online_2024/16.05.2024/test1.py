def automatic(n):
    b = bin(n)[2:]
    o = oct(n)[2:]
    if int(o[-1]) % 2 == 0:
        b = b + '10'
    else:
        b = b + '11'
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    r = int(b, 2)
    h = hex(r)[2:]
    return h


k = 0
a, b = map(int, input().split())
for i in range(a, b + 1):
    if len(automatic(i)) == 3:
        k += 1
print(k)
def n10inx(num, sys):
    x = ''
    while num > 0:
        x = str(num % sys) + x
        num //= sys
    return x


print(n10inx(321, 5))
print(bin(321)[2:])
print(hex(1236)[2:])
print(oct(1236)[2:])
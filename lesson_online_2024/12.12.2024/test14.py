m = 0
for x in range(0, 190):
    for y in range(0,190):
        a = int('W', 36) * 190**0 + x * 190**1 + int('N', 36) * 190**2
        b = int('R', 36) * 190**0 + 10 * 190**1 + y * 190**2 + int('Y', 36) * 190**3
        if (a + b) % 189 == 0:
            if x * y > m:
                m = x * y
                print(x * y, (a + b) // 189)
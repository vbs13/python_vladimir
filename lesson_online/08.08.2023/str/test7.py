text = input()
maxb = 0
b = 0

for i in text:
    if i != ' ':
        b += 1
        if b > maxb:
            maxb = b
    else:
        b = 0
print(maxb)



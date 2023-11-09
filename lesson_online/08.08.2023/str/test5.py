text = input()
big = 0
lit = 0

for i in text:
    if i == 'Ы':
        big += 1
    elif i == 'ы':
        lit += 1

print(big, lit)
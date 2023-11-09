a = [1, 2, 3, 4, 5]
b = []

kol = int(input())

for i in range(len(a)):
    b.append(a[(i - kol) % len(a)])

print(a)
print(b)
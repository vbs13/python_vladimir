a = [5, 4, 3, 2, 1]
print(a)

for y in range(len(a)):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

print(a)
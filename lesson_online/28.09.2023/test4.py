a = [1, 2, 3, 4, 5]

for i in range(len(a) - 1):
    print(a[i], a[i + 1])

for i in range(1, len(a)- 1):
    print(a[i - 1], a[i], a[i + 1])
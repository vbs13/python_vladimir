a = [1, 22, 3]

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        print(a[i], a[j])
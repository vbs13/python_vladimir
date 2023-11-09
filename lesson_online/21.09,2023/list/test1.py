a = [1, 2, 3, 12, 109, 0, 4]

print(a)

print(a[1], a[3:5])

a[1] = 7
a.append(777)
a.append(13)
a.sort()

print(a)

a.pop(2)
a.remove(109)

print(a)
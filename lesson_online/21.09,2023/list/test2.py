a = []
for i in range(1, 11):
    a.append(i)
print(a)

b = 0
for i in a:
    b += i
print(b)

print(sum(a))

maxx = 0
for i in a:
    if i > maxx:
        maxx = i
print(maxx)

print(max(a), min(a))
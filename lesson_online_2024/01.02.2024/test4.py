s = list(map(int, input().split()))

mas = [x for x in range(len(s)) if s[x] % 2 == 0]
mas1 = sorted([s[x] for x in mas])

k = 0
for i in mas:
    s[i] = mas1[k]
    k += 1

print(*s)

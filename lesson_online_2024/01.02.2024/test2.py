s = list(map(int, input().split()))
k = 0

for i in range(1, len(s) - 1):
    if s[i]**2 == (i + 1) * 2 or s[i]**2 == (i - 1) * 2:
        k += 1

print(k)

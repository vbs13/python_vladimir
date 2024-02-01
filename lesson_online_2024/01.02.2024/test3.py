s = list(map(int, input().split()))
white = []
black = []

for i in s:
    if i % 2 != 0 and '5' in str(i) and '6' not in str(i) or i == 0:
        white.append(i)
    if i % 2 == 0 and '6' in str(i) or i == 0:
        black.append(i)

print(*white)
print(*black)
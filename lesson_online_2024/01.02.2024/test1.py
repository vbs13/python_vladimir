s = list(map(int, input().split()))
# mas = [str(x) for x in s if x % 3 == 0 and abs(x) % 10 == 6]
mas = []

for x in s:
    if x % 3 == 0 and abs(x) % 10 == 6:
        mas.append(str(x))
print(','.join(mas))
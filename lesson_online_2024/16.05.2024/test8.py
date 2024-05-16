n, m = input().split()

mas = [list(map(int, input().split())) for x in range(int(n))]
# print(mas)
k = 0
res = []

for elem in mas:
    if sum(elem) >= k:
        k = sum(elem)
        res = elem

r = 0
for n in res:
    if n % 15 == 10:
        r += 1
print(r)

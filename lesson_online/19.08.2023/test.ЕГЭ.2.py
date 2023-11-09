n = int(input())
a = 2

for i in range(2, n//2 + 1):
    if n % i == 0:
        a += 1
print(a)
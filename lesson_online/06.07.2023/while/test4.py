k3 = 0
k = 0

while True:
    num = int(input())
    k += 1
    if num == 0:
        k -= 1
        break
    elif num % 3 == 0:
        k3 += 1

print(k, k3)
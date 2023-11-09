a = int(input())
b = int(input())
summ = 0
num = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        summ += i
        num += 1

print(summ / num)